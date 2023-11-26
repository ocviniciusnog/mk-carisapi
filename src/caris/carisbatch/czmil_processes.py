
"""
CZMIL Processes Module

This module extends the CarisBatchCommand class to provide specialized processes 
for handling Coastal Zone Mapping and Imaging Lidar (CZMIL) data. The module 
encompasses a variety of classes designed to classify, compare, convert, export, 
filter, georeference, import, optimize, and update CZMIL data.

Each class in this module is tailored for specific aspects of CZMIL data processing, 
from noise classification and reflectance optimization to the conversion of CZMIL 
raw data and the generation of georeferenced point clouds. These tools are essential 
for ensuring the accuracy and usability of CZMIL data in coastal and underwater 
mapping projects.

The module facilitates the integration and manipulation of CZMIL data within the b
roader framework of geospatial data processing, contributing to enhanced data 
quality and reliability in environmental and geographical analyses.

Author: Vinicius Nogueira
Created: 15-July-2020
Last Modified: 23-November-2023

Note:
    This module is an integral part of the MK-CarisAPI.
"""

from ._carisbatch import CarisBatchCommand

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Classify CZMIL Noise
class ClassifyCZMILNoise(CarisBatchCommand):
    """
    The ClassifyCZMILNoise class reads CZMIL data, breaks it into voxels and sends it to a classification algorithm locally. 
    Points are then given a Noise Confidence and filtered based on the specified threshold.

    Attributes:
        _command (str): The command associated with the 'Classify CZMIL Noise' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ClassifyCZMILNoise'
    _option_key = None

    _common_settings = {
        "noise_confidence_filter_threshold": None
    }

    class _ClassifyCZMILNoiseSettings:
        """
        Nested class for ClassifyCZMILNoise settings.
        """
        default_settings = {}

    _option_registry = {
        'CLASSIFYCZMILNOISE': _ClassifyCZMILNoiseSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Compare CZMIL to Reference
class CompareCZMILToReference(CarisBatchCommand):
    """
    The CompareCZMILToReference class is used to compare CZMIL format points to known reference points, 
    analyzing differences in depth and other attributes.

    Attributes:
        _command (str): The command associated with the 'Compare CZMIL to Reference' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CompareCZMILToReference'
    _option_key = None

    _common_settings = {
        "reference_points": None,
        "reference_radius": None,
        "vertical_tolerance_filter": None,
        "x_axis": None,
        "y_axis": None,
        "shallow_image_file": None,
        "deep_image_file": None,
        "shallow_image": None,
        "deep_image": None,
        "number_of_shallow_points": None,
        "number_of_deep_points": None,
        "number_of_filtered_shallow_points": None,
        "number_of_filtered_deep_points": None,
        "percentage_of_shallow_points_within_limit": None,
        "percentage_of_deep_points_within_limit": None
    }

    class _CompareCZMILToReferenceSettings:
        """
        Nested class for CompareCZMILToReference settings.
        """
        default_settings = {}

    _option_registry = {
        'COMPARECZMILTOREFERENCE': _CompareCZMILToReferenceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Compute CZMIL Calibration
class ComputeCZMILCalibration(CarisBatchCommand):
    """
    The ComputeCZMILCalibration class processes CZMIL data through automated lidar calibration, 
    computing values for application in the Georeference CZMIL Points process.

    Attributes:
        _command (str): The command associated with the 'Compute CZMIL Calibration' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ComputeCZMILCalibration'
    _option_key = None

    _common_settings = {
        "survey_folder": None,
        "lidar_corrections": None,
        "ground_control_points_file": None
    }

    class _ComputeCZMILCalibrationSettings:
        """
        Nested class for ComputeCZMILCalibration settings.
        """
        default_settings = {}

    _option_registry = {
        'COMPUTECZMILCALIBRATION': _ComputeCZMILCalibrationSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Convert CZMIL Camera Images
class ConvertCZMILCameraImages(CarisBatchCommand):
    """
    The ConvertCZMILCameraImages class generates images in various formats from CZMIL IIQ files.

    Attributes:
        _command (str): The command associated with the 'Convert CZMIL Camera Images' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ConvertCZMILCameraImages'
    _option_key = None

    _common_settings = {
        "OutputFolder": None,
        "OutputFormat": None,
        "JPEGQuality": None,
        "resolution": None,
        "resolution_unit": None,
        "bits": None,
        "rotation": None,
        "brightness": None,
        "contrast": None,
        "saturation": None,
        "level_highlight": None,
        "level_shadow": None,
        "target_highlight": None,
        "target_shadow": None,
        "highlight_recovery": None,
        "shadow_recovery": None,
        "clarity": None,
        "enable_open_cl": None,
        "output_profile": None,
        "tif_compression": None,
        "lcc_skip_dust_removal": None,
        "lcc_technical_camera": None,
        "input_profile": None,
        "file_curve": None,
        "scale": None,
        "orientation": None,
        "kelvin": None,
        "tint": None,
        "exposure": None,
        "level_highlight_r": None,
        "level_highlight_g": None,
        "level_highlight_b": None,
        "level_shadow_r": None,
        "level_shadow_g": None,
        "level_shadow_b": None,
        "midtone_r": None,
        "midtone_g": None,
        "midtone_b": None,
        "midtone": None
    }

    class _ConvertCZMILCameraImagesSettings:
        """
        Nested class for ConvertCZMILCameraImages settings.
        """
        default_settings = {}

    _option_registry = {
        'CONVERTCZMILCAMERAIMAGES': _ConvertCZMILCameraImagesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Convert CZMIL Raw
class ConvertCZMILRAW(CarisBatchCommand):
    """
    The ConvertCZMILRAW class converts Coastal Zone Mapping and Imaging Lidar (CZMIL) data from RAW format to CWF format.

    Attributes:
        _command (str): The command associated with the 'Convert CZMIL Raw' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ConvertCZMILRAW'
    _option_key = None

    _common_settings = {
        "time_offset": None
    }

    class _ConvertCZMILRAWSettings:
        """
        Nested class for ConvertCZMILRAW settings.
        """
        default_settings = {}

    _option_registry = {
        'CONVERTCZMILRAW': _ConvertCZMILRAWSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export CZMIL to LAS
class ExportCZMILToLAS(CarisBatchCommand):
    """
    The ExportCZMILToLAS class exports band values from input points in CZMIL (CPF) format to an LAS file.

    Attributes:
        _command (str): The command associated with the 'Export CZMIL to LAS' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportCZMILToLAS'
    _option_key = None

    _common_settings = {
        "las_version": None,
        "point_record_format": None,
        "include_band": None,
        "coordinate_precision": None,
        "elevation_precision": None,
        "pulse_reflection_suppression_factor": None,
        "waveform": None,
        "channel": None,
        "include_rejected": None,
        "use_gps_week_time": None,
        "override_classification_file": None,
        "override_classification_mapping": None,
        "output_crs": None,
        "include_mapping_index": None,
        "include_circular_scan_angle": None,
        "include_approximate_scan_angle": None,
        "include_scan_angle_direction": None,
        "clamped_return_number": None,
        "suppression_factor": None
    }

    class _ExportCZMILToLASSettings:
        """
        Nested class for ExportCZMILToLAS settings.
        """
        default_settings = {}

    _option_registry = {
        'EXPORTCZMILTOLAS': _ExportCZMILToLASSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export CZMIL Waveforms
class ExportCZMILWaveforms(CarisBatchCommand):
    """
    The ExportCZMILWaveforms class exports a subset of the waveforms in a CZMIL dataset.

    Attributes:
        _command (str): The command associated with the 'Export CZMIL Waveforms' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportCZMILWaveforms'
    _option_key = None

    _common_settings = {
        "output_folder": None,
        "start_record_number": None,
        "number_of_records": None
    }

    class _ExportCZMILWaveformsSettings:
        """
        Nested class for ExportCZMILWaveforms settings.
        """
        default_settings = {}

    _option_registry = {
        'EXPORTCZMILWAVEFORMS': _ExportCZMILWaveformsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter CZMIL Points
class FilterCZMILPoints(CarisBatchCommand):
    """
    The FilterCZMILPoints class applies an uncertainty threshold to reject CZMIL Points data 
    that fall outside the specified threshold. It can also filter by a direct threshold amount.

    Attributes:
        _command (str): The command associated with the 'Filter CZMIL Points' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FilterCZMILPoints'
    _option_key = None

    _common_settings = {
        "include_rejected": None,
        "threshold": None
    }

    class _FilterCZMILPointsSettings:
        """
        Nested class for FilterCZMILPoints settings.
        """
        default_settings = {}

    _option_registry = {
        'FILTERCZMILPOINTS': _FilterCZMILPointsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Georeference CZMIL Points
class GeoreferenceCZMILPoints(CarisBatchCommand):
    """
    The GeoreferenceCZMILPoints class converts CZMIL CWF waveform and SBET trajectory data 
    into a georeferenced point cloud, applying roll, pitch, and heading corrections to 
    generate point cloud data referenced to ellipsoid height. Each point is assigned a 
    land/water confidence value for identifying land or water points, essential in 
    determining the seafloor.

    Attributes:
        _command (str): The command associated with the 'Georeference CZMIL Points' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'GeoreferenceCZMILPoints'
    _option_key = None

    _common_settings = {
        "sbet_file": None,
        "sbet_file_coordinate_reference_system": None,
        "water_surface_control": None
    }

    class _GeoreferenceCZMILPointsSettings:
        """
        Nested class for GeoreferenceCZMILPoints settings.
        """
        default_settings = {}

    _option_registry = {
        'GEOREFERENCECZMILPOINTS': _GeoreferenceCZMILPointsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import CZMIL to Survey
class ImportCZMILToSurvey(CarisBatchCommand):
    """
    The ImportCZMILToSurvey class imports a CZMIL mission execution file and raw information 
    to create a new survey file. It handles the processing and conversion of CZMIL LRAW files 
    and associated flight lines as per the provided mission execution details.

    Attributes:
        _command (str): The command associated with the 'Import CZMIL to Survey' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportCZMILToSurvey'
    _option_key = None

    _common_settings = {
        "mission_execution_file": None,
        "camera_raw_folder": None,
        "processing_folder": None,
        "survey_name": None,
        "buffer_time": None,
        "sbet_files": [],
        "sbet_rms_files": [],
        "output_crs": None
    }

    class _ImportCZMILToSurveySettings:
        """
        Nested class for ImportCZMILToSurvey settings.
        """
        default_settings = {}

    _option_registry = {
        'IMPORTCZMILTOSURVEY': _ImportCZMILToSurveySettings
    }

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import CZMIL Raw to Survey
class ImportCZMILRawToSurvey(CarisBatchCommand):
    """
    The ImportCZMILRawToSurvey class imports CZMIL raw data from a specified raw folder 
    and creates a new survey file. It processes the raw lidar data and associated files 
    to generate a comprehensive survey dataset.

    Attributes:
        _command (str): The command associated with the 'Import CZMIL Raw to Survey' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportCZMILRawToSurvey'
    _option_key = None

    _common_settings = {
        "lidar_raw_folder": None,
        "camera_raw_folder": None,
        "processing_folder": None,
        "survey_name": None,
        "sbet_files": [],
        "sbet_rms_files": [],
        "output_crs": None
    }

    class _ImportCZMILRawToSurveySettings:
        """
        Nested class for ImportCZMILRawToSurvey settings.
        """
        default_settings = {}

    _option_registry = {
        'IMPORTCZMILRAWTOSURVEY': _ImportCZMILRawToSurveySettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optimize CZMIL Reflectance
class OptimizeCZMILReflectance(CarisBatchCommand):
    """
    The OptimizeCZMILReflectance class processes CZMIL data through an algorithm to 
    radiometrically balance the Shallow channels and optimize the reflectance values, 
    using ground control points and other parameters.

    Attributes:
        _command (str): The command associated with the 'Optimize CZMIL Reflectance' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'OptimizeCZMILReflectance'
    _option_key = None

    _common_settings = {
        "ground_control_points_file": None,
        "relative_difference_threshold": None,
        "relative_difference_percentage": None,
        "search_radius_shallow": None,
        "search_radius_deep": None,
        "min_control_points_shallow": None,
        "min_control_points_deep": None
    }

    class _OptimizeCZMILReflectanceSettings:
        """
        Nested class for OptimizeCZMILReflectance settings.
        """
        default_settings = {}

    _option_registry = {
        'OPTIMIZECZMILREFLECTANCE': _OptimizeCZMILReflectanceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update CZMIL Deep Channel Range Offset
class UpdateCZMILDeepChannelRangeOffset(CarisBatchCommand):
    """
    The UpdateCZMILDeepChannelRangeOffset class estimates and updates the deep channel range offset 
    in a CZMIL dataset, modifying the associated LCP file based on processed CZMIL CPF file data.

    Attributes:
        _command (str): The command associated with the 'Update CZMIL Deep Channel Range Offset' process.
        _option_key (str): Key to identify specific settings for the process, set to None as this process has no additional options.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateCZMILDeepChannelRangeOffset'
    _option_key = None

    _common_settings = {}

    class _UpdateCZMILDeepChannelRangeOffsetSettings:
        """
        Nested class for UpdateCZMILDeepChannelRangeOffset settings.
        """
        default_settings = {}

    _option_registry = {
        'UPDATECZMILDEEPCHANNELRANGEOFFSET': _UpdateCZMILDeepChannelRangeOffsetSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update CZMIL from LAS
class UpdateCZMILFromLAS(CarisBatchCommand):
    """
    The UpdateCZMILFromLAS class updates CZMIL attributes in a CPF file based on specified attributes 
    from one or more LAS files. This process requires that the LAS files were exported with the IncludeMappingIndex 
    option enabled in the Export CZMIL to LAS process.

    Attributes:
        _command (str): The command associated with the 'Update CZMIL from LAS' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateCZMILFromLAS'
    _option_key = None

    _common_settings = {
        "data": None
    }

    class _UpdateCZMILFromLASSettings:
        """
        Nested class for UpdateCZMILFromLAS settings.
        """
        default_settings = {}

    _option_registry = {
        'UPDATECZMILFROMLAS': _UpdateCZMILFromLASSettings
    }
