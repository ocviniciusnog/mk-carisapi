
"""
Caris Batch Command Module

This module provides the CarisBatchCommand class which is used for managing and executing
Caris batch commands. It handles the construction of command strings, execution of
commands via subprocesses, and provides robust error handling and logging capabilities.

Author: Vinicius Nogueira
Created: 15-July-2020
Last Modified: 23-November-2023

"""

from pathlib import Path as _Path
import subprocess as _subprocess
from ._utils import Dispatcher as _Dispatcher
from ._utils import ensure_iterable as _ensure_iterable
from types import GeneratorType as _GeneratorType

class CarisBatchError(Exception):
    """
    Custom exception class for errors related to Caris Batch operations.
    
    This exception is raised when specific errors related to Caris Batch command
    execution and configuration occur.
    """
    
    pass

class CarisBatchCommand:
    """
    A class to manage and execute Caris batch commands.

    Handles the construction and execution of commands for Caris batch processing,
    including managing input and output settings, and running the command with subprocess.

    Attributes:
        input (str, Path): The input file or directory.
        input_as_uri (bool): Flag to determine if the input is a URI.
        vessels (str, optional): Vessel identifiers for the command.
        days (str, optional): Day identifiers for the command.
        lines (str, optional): Line identifiers for the command.
        files_to_load (list): List of files to be loaded.
        output (str, Path): The output file or directory.
        output_as_uri (bool): Flag to determine if the output is a URI.
        settings (dict): Configuration settings for the command.
    """
    
    _dispatcher = None
    
    def __init__(self, **kwargs):
        """
        Initializes the CarisBatchCommand object with provided arguments.

        Args:
            **kwargs: Arbitrary keyword arguments. Supported arguments include
                      'input', 'input_as_uri', 'vessel', 'day', 'line',
                      'files_to_load', 'output', and 'output_as_uri'.
        """
        
        self.input = kwargs.pop('input', None)
        self.input_as_uri = kwargs.pop('input_as_uri', False)

        self.vessels = kwargs.pop('vessel', None)
        self.days = kwargs.pop('day', None)
        self.lines = kwargs.pop('line', None)

        self.files_to_load = list(kwargs.pop('files_to_load', []))

        self.output = kwargs.pop('output', None)
        self.output_as_uri = kwargs.pop('output_as_uri', False)
        
        if CarisBatchCommand._dispatcher is None:
            CarisBatchCommand._dispatcher = self._initialize_dispatcher()
            
        self.settings = None
    
    @property
    def _repeatable_args(self):
        return ("area_features", "attribute", "blocking_feature", "channel", "compare",
                "component_attribute", "compute_band", "contour_features", "coordinate_format",
                "contributor_attribute", "data", "deep_attributes", "filter_acquisition",
                "filter_post_processing", "grazing_angle_table", "import_type", "include",
                "include_3D_symbol", "include_attribute", "include_band", "include_flag",
                "input_band", "level", "level_file", "matrix", "minimum_distance", "overwrite",
                "override_classification_mapping", "range", "range_table", "reference_area_features",
                "reference_features", "reject_quality", "reject_type", "sbet_files", "sbet_rms_files",
                "shoal_attributes", "smooth_sensor", "status", "surface_name", "svp", "template",
                "template_name")
    
    class _ArgsProcessing:
        """
        A nested class for processing various types of arguments for the Caris batch command.
        
        This class provides static methods for processing different types of arguments
        into the format required by the Caris batch command.
        """
        
        @staticmethod
        def iterables(key, values):
            return [f'--{key.replace("_","-")}'] + [f'"{value}"' for value in values]
        
        @staticmethod
        def common_types(key, value):
            return [f'--{key.replace("_","-")} "{value}"']

        @staticmethod
        def booleans(key, value):
            return [f'--{key.replace("_","-")}' if value else None]
        
        @staticmethod
        def repeatables_args(key, values):
            values = _ensure_iterable(values)
            return [f'--{key.replace("_","-")} "{value}"' for value in values]
        
        @staticmethod
        def files_to_load(files):
            return [f'"{str(f)}"' for f in _ensure_iterable(files) or [] if f]
        
        @staticmethod
        def proc_path(path, as_uri=False, vessels=None, days=None, lines=None):
            if not path:
                return []
            
            path = _Path(path)
            uri = path.as_uri() if as_uri else str(path)
            
            if as_uri and uri.endswith('.hips'):
                query_params = ";".join(
                    f"{param}={value}"
                    for param, values in [('Vessel', vessels), ('Day', days), ('Line', lines)]
                    for value in _ensure_iterable(values) if value)
                
                return [f'"{uri}?{query_params}"' if query_params else f'"{uri}"']
            
            return [f'"{uri}"']
    
    @staticmethod
    def _initialize_dispatcher():
        """
        Initializes and returns a dispatcher for argument processing.

        The dispatcher maps different types of arguments to their respective
        processing methods in the _ArgsProcessing class.

        Returns:
            _Dispatcher: An instance of the dispatcher with registered processing methods.
        """
        dispatcher = _Dispatcher()
        dispatcher.register('Repeatable', CarisBatchCommand._ArgsProcessing.repeatables_args)
        dispatcher.register(bool, CarisBatchCommand._ArgsProcessing.booleans)
        dispatcher.register(list, CarisBatchCommand._ArgsProcessing.iterables)
        dispatcher.register(tuple, CarisBatchCommand._ArgsProcessing.iterables)
        dispatcher.register(_GeneratorType, CarisBatchCommand._ArgsProcessing.iterables)
        dispatcher.register(int, CarisBatchCommand._ArgsProcessing.common_types)
        dispatcher.register(str, CarisBatchCommand._ArgsProcessing.common_types)
        dispatcher.register(float, CarisBatchCommand._ArgsProcessing.common_types)
        
        return dispatcher
        
    
    def config(self, **kwargs):
        """
        Configures the settings for the Caris batch command.

        Args:
            **kwargs: Arbitrary keyword arguments for settings configuration.

        Raises:
            CarisBatchError: If an unsupported option is provided.
        """
        kwargs = {key.replace('-', '_').lstrip('_'): value for key, value in kwargs.items()}
        
        if self.settings is None:
            self.settings = {}
        
        if self._option_key in kwargs and self.settings.get(self._option_key) != kwargs[self._option_key]:
            self.settings = None
        
        if not self.settings:
            option = kwargs.get(self._option_key, self._command)
            self._set_config(option, **kwargs)
        else:
            self._update_settings(kwargs)

    def _set_config(self, option, **kwargs):
        """
        Sets the configuration for a given option.

        Args:
            option (str): The option key to set.
            **kwargs: Arbitrary keyword arguments for setting the configuration.

        Raises:
            CarisBatchError: If the option is unsupported.
        """
        
        settings_class = self._option_registry.get(option.upper())
        if not settings_class:
            raise CarisBatchError(f'Unsupported option: {option}')

        self.settings = {**self._common_settings, **settings_class.default_settings}
        self._update_settings(kwargs)

    def _update_settings(self, kwargs):
        """
        Updates the current settings with provided key-value pairs.

        Args:
            kwargs (dict): A dictionary of settings to update.

        Raises:
            CarisBatchError: If a setting key is invalid.
        """
        
        for key, value in kwargs.items():
            if key in self.settings:
                self.settings[key] = value
            else:
                raise CarisBatchError(f"Invalid setting: '{key}' is not a valid option for {self.settings.get(self._option_key, 'unknown')}")
        
    def get_cmd(self):
        """
        Constructs and returns the Caris batch command string based on the current settings.

        Returns:
            str: The constructed command string.

        Raises:
            CarisBatchError: If the settings are not properly configured.
        """
        if self.input is None and self.output is None:
            raise CarisBatchError("Input and/or output are not configured")
            
        if not self.settings and self._option_key is not None:
            raise CarisBatchError("Settings are not configured")
            
        args_list = ['carisbatch', '--run', str(self._command)]

        for key, value in self.settings.items():
            if value:
                if key in self._repeatable_args:
                    args_list += self._dispatcher.dispatch('Repeatable', key, value)
                else:
                    args_list += self._dispatcher.dispatch(type(value), key, value)

        input = self._ArgsProcessing.proc_path(
            path=self.input,as_uri=self.input_as_uri,
            vessels=self.vessels, days=self.days, lines=self.lines)

        output = self._ArgsProcessing.proc_path(
            path=self.output,as_uri=self.output_as_uri)

        files_to_load = self._ArgsProcessing.files_to_load(files=self.files_to_load)

        command = ' '.join(args_list + files_to_load + input + output)
        
        return command

    def run(self, timeout=3600):
        """
        Executes the Caris batch command as a subprocess.

        Args:
            timeout (int): The timeout in seconds for the command execution.

        Returns:
            tuple: A tuple containing the return code, stdout, stderr, and command.

        Raises:
            CarisBatchError: If an error occurs during command execution.
        """
        command = self.get_cmd()
        process = None

        try:
            process = _subprocess.Popen(
                command, shell=True, stdout=_subprocess.PIPE, 
                stderr=_subprocess.PIPE, text=True)

            stdout, stderr = process.communicate(timeout=timeout)
            return (process.returncode, stdout, stderr, command)
    
        except _subprocess.TimeoutExpired:
            if process:
                process.kill()
                process.communicate()  # Ensures resources are cleaned up
            return (1, '', 'Command Timed out', command)
        except CarisBatchError as e:
            return (-1, '', f'An error occurred: {e}', command)
        finally:
            if process:
                process.stdout.close()
                process.stderr.close()