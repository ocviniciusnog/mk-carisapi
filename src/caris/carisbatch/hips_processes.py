
"""
HIPS Processes Module

This module extends the CarisBatchCommand class to provide specialized functionalities 
for Hydrographic Information Processing System (HIPS) operations. It encompasses 
a diverse array of classes, each tailored to handle specific tasks within hydrographic 
data processing workflows, such as adding Kraken TIL to mosaics, managing HIPS grids, 
and updating SIPS contact positions.

Each class within this module encapsulates the necessary commands and parameters 
to facilitate a wide range of hydrographic data processing tasks. From integrating 
intensity bands and managing raster mosaics to noise classification and bathymetric 
data filtering, these classes are designed to ensure precision and efficiency in 
hydrographic data processing.

Author: Vinicius Nogueira
Created: 15-July-2020
Last Modified: 23-November-2023

Note:
    This module is an integral part of the MK-CarisAPI.
"""

from ._carisbatch import CarisBatchCommand

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add Kraken TIL To Mosaic
class AddKrakenTILToMosaic(CarisBatchCommand):
    """
    The AddKrakenTILToMosaic class manages the process of adding intensity bands from Kraken *.TIL files 
    to an existing raster mosaic. This process is used to update a Kraken mosaic with data from 
    one or more Kraken *.TIL files.

    Since there are no specific options for this process, the class includes a nested class 
    for the command settings, but without any specific settings.

    Attributes:
        _command (str): The command associated with the 'Add Kraken TIL To Mosaic' process.
        _option_key (None): Indicates the absence of a specific option key.
        _common_settings (dict): Empty dictionary, as there are no common settings.
        _option_registry (dict): Registry mapping the command to its settings class in uppercase.
    """

    _command = 'AddKrakenTILToMosaic'
    _option_key = None

    _common_settings = {}

    class AddKrakenTILToMosaicSettings:
        """
        Nested class for AddKrakenTILToMosaic settings. 
        """
        default_settings = {}

    _option_registry = {
        'ADDKRAKENTILTOMOSAIC': AddKrakenTILToMosaicSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add To HIPS Grid
class AddToHIPSGrid(CarisBatchCommand):
    """
    The AddToHIPSGrid class is designed for adding HIPS track lines to an existing HIPS surface. 
    It utilizes the create process parameters stored in the CSAR metadata to update the HIPS surface.

    This class encapsulates the command and parameters for the AddToHIPSGrid process, enabling the 
    updating of a HIPS surface with data from one or more HIPS track lines.

    Attributes:
        _command (str): The command associated with the 'Add To HIPS Grid' process.
        _option_key (None): No specific option key as there are no additional options.
        _common_settings (dict): Empty dictionary, as there are no common settings.
        _option_registry (dict): Registry mapping the command to its settings class in uppercase.
    """

    _command = 'AddToHIPSGrid'
    _option_key = None

    _common_settings = {}

    class AddToHIPSGridSettings:
        """
        Nested class for AddToHIPSGrid settings. 
        """
        default_settings = {}

    _option_registry = {
        'ADDTOHIPSGRID': AddToHIPSGridSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add To SIPS Mosaic
class AddToSIPSMosaic(CarisBatchCommand):
    """
    The AddToSIPSMosaic class is designed for adding HIPS sources to an existing raster mosaic using 
    the process parameters. It updates the SIPS mosaic with data from one or more HIPS track lines.

    Attributes:
        _command (str): The command associated with the 'Add To SIPS Mosaic' process.
        _option_key (str): Key to identify specific mosaic engine options.
        _common_settings (dict): Dictionary containing the common settings for the process.
        _option_registry (dict): Registry mapping the command to its settings classes.
    """

    _command = 'AddToSIPSMosaic'
    _option_key = 'mosaic_engine'

    _common_settings = {
        "mosaic_engine": None,
        "blending": None,
        "weighting": None
    }

    class SIPSBackscatterSettings:
        default_settings = {
            "imagery": None,
            "avg": None,
            "avg_normalization_range": None,
            "beam_pattern_file": None,
            "beam_pattern_file_operation": None,
            "correct_for_acquisition_mode": None,
            "s7k_compensated_data": None,
            "local_absorption": None,
            "filter_angle_t1": None,
            "filter_t1": None,
            "filter_angle_t2": None,
            "filter_t2": None,
            "surface": None,
            "filter": None,
            "sound_velocity": None,
            "corrections_text_folder": None
        }

    class SIPSBackscatterWMAAreaAVGSettings:
        default_settings = {}

    class SIPSSideScanSettings:
        default_settings = {
            "channel": None,
            "beam_pattern": None,
            "beam_pattern_file": None,
            "gain": None,
            "tvg": None,
            "gain_normalization": None,
            "despeckle": None,
            "ratio_filter": None,
            "ratio_filter_limit": None,
            "across_distance_limit": None,
            "filter": None,
            "extrapolate_time": None,
            "registration_bathy": None,
            "gyro_source": None,
            "smooth_gyro": None,
            "sound_velocity": None,
            "altitude_offset": None,
            "correct_for_pitch": None
        }

    class GeocoderSettings:
        default_settings = {
            "channel": None,
            "imagery": None,
            "anti_alias": None,
            "gain": None,
            "tvg": None,
            "avg": None,
            "avg_window_size": None,
            "despeckle": None,
            "nadir_angle": None,
            "filter": None,
            "surface": None,
            "smooth_gyro": None
        }

    _option_registry = {
        'SIPS_BACKSCATTER': SIPSBackscatterSettings,
        'SIPS_BACKSCATTER_WMA_AREA_AVG': SIPSBackscatterWMAAreaAVGSettings,
        'SIPS_SIDESCAN': SIPSSideScanSettings,
        'GEOCODER': GeocoderSettings,
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Classify HIPS Noise
class ClassifyHIPSNoise(CarisBatchCommand):
    """
    The ClassifyHIPSNoise class is designed to identify and remove noise from bathymetric data using 
    a pre-trained Convolutional Neural Network (CARIS Mira AI). It assigns a Noise Confidence value to 
    each point and can filter points based on this value.

    Attributes:
        _command (str): The command associated with the 'Classify HIPS Noise' process.
        _option_key (str): Key to identify specific settings for noise classification.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ClassifyHIPSNoise'
    _option_key = None

    _common_settings = {
        "mira_url": "http://username:password@carismira.ai",
        "finest_vertical_resolution": 0.1,
        "noise_confidence_filter_threshold": None,
        "level_of_detail": "Medium"
    }

    class _NoSpecificOptions:
        default_settings = {}

    _option_registry = {
        'default': _NoSpecificOptions
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Compare HIPS
class CompareHIPS(CarisBatchCommand):
    """
    The CompareHIPS class is used to compare two HDCS lines in various aspects such as bathymetry, 
    navigation, motion, and sidescan. It provides options to set tolerances and types of data to compare.

    Attributes:
        _command (str): The command associated with the 'Compare HIPS' process.
        _option_key (str): Key to identify specific settings for the comparison.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CompareHIPS'
    _option_key = None

    _common_settings = {
        "compare": "ALL",
        "backscatter_precision": None,
        "bathymetry_precision": None,
        "ignore_rejected": None,
        "motion_precision": None,
        "navigation_precision": None,
        "sidescan_precision": None,
        "navigation_geometry": None
    }

    class CompareHIPS_Settings:
        default_settings = {}

    _option_registry = {
        'ALL': CompareHIPS_Settings,
        'BATHYMETRY': CompareHIPS_Settings,
        'NAVIGATION': CompareHIPS_Settings,
        'MOTION': CompareHIPS_Settings,
        'SIDESCAN': CompareHIPS_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Compute HIPS Separation Model
class ComputeHIPSSeparationModel(CarisBatchCommand):
    """
    The ComputeHIPSSeparationModel class is used to create a separation model in CSAR format using HIPS data with Tide loaded.

    Attributes:
        _command (str): The command associated with the 'Compute HIPS Separation Model' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ComputeHIPSSeparationModel'
    _option_key = None

    _common_settings = {
        "resolution": None,
        "smooth_height": None,
        "dynamic_heave": None,
        "mru_remote_heave": None,
        "antenna_offset": None,
        "dynamic_draft": None,
        "vehicle_depth": None,
        "waterline": None,
        "height_correction": None,
        "time_offset": None
    }

    class ComputeHIPSSeparationModel_Settings:
        default_settings = {}

    _option_registry = {
        'COMPUTEHIPSSEPARATIONMODEL': ComputeHIPSSeparationModel_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Compute SIPS Towfish Navigation
class ComputeSIPSTowfishNavigation(CarisBatchCommand):
    """
    The ComputeSIPSTowfishNavigation class is used to compute the position of a towfish from the ship's navigation using a horizontal distance and direction from the ship's towpoint to the towfish.

    Attributes:
        _command (str): The command associated with the 'Compute SIPS Towfish Navigation' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ComputeSIPSTowfishNavigation'
    _option_key = None

    _common_settings = {
        "smooth_sensor": None,
        "use_cmg": None,
        "recompute_contact_positions": None
    }

    class ComputeSIPSTowfishNavigation_Settings:
        default_settings = {}

    _option_registry = {
        'COMPUTESIPSTOWFISHNAVIGATION': ComputeSIPSTowfishNavigation_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Compute HIPS Boresight Calibration
class ComputeHIPSBoresightCalibration(CarisBatchCommand):
    """
    The ComputeHIPSBoresightCalibration class is used for automatic selection of the best planar areas from the sea floor and 
    computation of the boresight calibration values based on these areas.

    Attributes:
        _command (str): The command associated with the 'Compute HIPS Boresight Calibration' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ComputeHIPSBoresightCalibration'
    _option_key = None

    _common_settings = {
        "extent": None,
        "head_number": None,
        "max_patches": None,
        "min_observability": None,
        "update_vessel": None,
        "report_file": None
    }

    class ComputeHIPSBoresightCalibration_Settings:
        default_settings = {}

    _option_registry = {
        'COMPUTEHIPSBORESIGHTCALIBRATION': ComputeHIPSBoresightCalibration_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copy HIPS to HIPS
class CopyHIPStoHIPS(CarisBatchCommand):
    """
    The CopyHIPStoHIPS class is used for copying HIPS track lines from one HIPS file to another. 
    It includes options to carry over various types of data associated with the original HIPS file.

    Attributes:
        _command (str): The command associated with the 'Copy HIPS to HIPS' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CopyHIPStoHIPS'
    _option_key = None

    _common_settings = {
        "carry_over": None
    }

    class CopyHIPStoHIPS_Settings:
        default_settings = {}

    _option_registry = {
        'COPYHIPSTOHIPS': CopyHIPStoHIPS_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create HIPS File
class CreateHIPSFile(CarisBatchCommand):
    """
    The CreateHIPSFile class is used for creating a new HIPS file with specified CRS and extent, 
    or from a template. It outputs a *.hips file.

    Attributes:
        _command (str): The command associated with the 'Create HIPS File' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateHIPSFile'
    _option_key = None

    _common_settings = {
        "output_crs": None,
        "user": None,
        "description": None,
        "extent": None,
        "template_file": None
    }

    class CreateHIPSFileSettings:
        default_settings = {}

    _option_registry = {
        'CREATEHIPSFILE': CreateHIPSFileSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create HIPS Grid
class CreateHIPSGrid(CarisBatchCommand):
    """
    The CreateHIPSGrid class is used to create a raster surface using various HIPS gridding methods.

    Attributes:
        _command (str): The command associated with the 'Create HIPS Grid' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateHIPSGrid'
    _option_key = 'gridding_method'

    _common_settings = {
        "gridding_method": None,
        "auto_resolution": None,
        "resolution": None,
        "extent": None,
        "output_crs": None,
        "output_vertical_crs": None,
        "primary_band": None,
        "compute_band": None,
        "comments": None,
        "include_flag": None,
        "include_additional_bathymetry": None,
        "keep_up_to_date": None,
        "filter": None
    }

    class _SHOAL_TRUESettings:
        default_settings = {}

    class _SWATH_ANGLESettings:
        default_settings = {
            "max_footprint": None,
            "grazing_angle_file": None,
            "grazing_angle_table": None
        }

    class _UNCERTAINTYSettings:
        default_settings = {
            "iho_order": None,
            "iho_limits": None
        }

    class _CUBE_Settings:
        default_settings = {
            "iho_order": None,
            "iho_limits": None,
            "disambiguation_method": None,
            "cube_config_file": None,
            "cube_config_name": None,
            "cube_config_settings": None
        }

    _option_registry = {
        'SHOAL_TRUE': _SHOAL_TRUESettings,
        'SWATH_ANGLE': _SWATH_ANGLESettings,
        'UNCERTAINTY': _UNCERTAINTYSettings,
        'CUBE': _CUBE_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create HIPS Vessel File
class CreateHIPSVesselFile(CarisBatchCommand):
    """
    The CreateHIPSVesselFile class is used to create a HIPS Vessel file(s) from settings stored in raw data files converted into HIPS data.

    Attributes:
        _command (str): The command associated with the 'Create HIPS Vessel File' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateHIPSVesselFile'
    _option_key = None

    _common_settings = {
        "vessel_folder": None
    }

    class _CreateHIPSVesselFileSettings:
        """
        Nested class for handling settings specific to the CreateHIPSVesselFile process.
        """
        default_settings = {}

    _option_registry = {
        'CREATEHIPSVESSELFILE': _CreateHIPSVesselFileSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create SIPS Beam Pattern
class CreateSIPSBeamPattern(CarisBatchCommand):
    """
    The CreateSIPSBeamPattern class is used to create a beam pattern file that applies corrections to remove acoustic artifacts from imagery caused by sonar imperfections.

    Attributes:
        _command (str): The command associated with the 'Create SIPS Beam Pattern' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateSIPSBeamPattern'
    _option_key = 'mosaic_engine'

    _common_settings = {
        "mosaic_engine": None,
        "beam_pattern_file": None
    }

    class _SIPSBackscatterSettings:
        """
        Nested class for handling settings specific to the SIPS Backscatter engine in the CreateSIPSBeamPattern process.
        """
        default_settings = {
            "beam_pattern_file_operation": None,
            "s7k_compensated_data": None,
            "local_absorption": None,
            "nadir_angle_t1": None,
            "nadir_angle_t2": None,
            "surface": None
        }

    class _SIPSSideScanSettings:
        """
        Nested class for handling settings specific to the SIPS Side Scan engine in the CreateSIPSBeamPattern process.
        """
        default_settings = {}

    _option_registry = {
        'SIPS_BACKSCATTER': _SIPSBackscatterSettings,
        'SIPS_SIDESCAN': _SIPSSideScanSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create SIPS Mosaic
class CreateSIPSMosaic(CarisBatchCommand):
    """
    The CreateSIPSMosaic class is used to create a raster mosaic using different Processing Engines based on the HIPS track lines.

    Attributes:
        _command (str): The command associated with the 'Create SIPS Mosaic' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _option_key = 'mosaic_engine'
    _command = 'CreateSIPSMosaic'

    _common_settings = {
        "mosaic_engine": None,
        "resolution": None,
        "blending": None,
        "weighting": None,
        "output_crs": None,
        "editable": None,
        "extent": None
    }

    class _SIPSBackscatterSettings():

        default_settings = {
            "auto_resolution": None,
            "imagery": None,
            "avg": None,
            "avg_normalization_range": None,
            "beam_pattern_file": None,
            "beam_pattern_file_operation": None,
            "correct_for_acquisition_mode": None,
            "s7k_compensated_data": None,
            "local_absorption": None,
            "filter_angle_t1": None,
            "filter_t1": None,
            "filter_angle_t2": None,
            "filter_t2": None,
            "surface": None,
            "filter": None,
            "sound_velocity": None,
            "corrections_text_folder": None
        }

    class _SIPSBackscatterWMAAreaAvgSettings():

        default_settings = {
            "auto_resolution": None,
            "search_radius": None,
            "imagery": None,
            "area_avg": None,
            "avg_normalization_range": None,
            "updating_size": None,
            "chunk_size_multiplier": None,
            "avg_curve_source_time_series": None,
            "beam_pattern_file": None,
            "beam_pattern_file_operation": None,
            "correct_for_acquisition_mode": None,
            "s7k_compensated_data": None,
            "local_absorption": None,
            "filter_angle_t1": None,
            "filter_t1": None,
            "filter_angle_t2": None,
            "filter_t2": None,
            "surface": None,
            "filter": None,
            "sound_velocity": None
        }

    class _SIPSSideScanSettings():

        default_settings = {
            "channel": None,
            "beam_pattern": None,
            "beam_pattern_file": None,
            "gain": None,
            "tvg": None,
            "gain_normalization": None,
            "despeckle": None,
            "ratio_filter": None,
            "ratio_filter_limit": None,
            "across_distance_limit": None,
            "filter": None,
            "extrapolate_time": None,
            "registration_bathy": None,
            "gyro_source": None,
            "smooth_gyro": None,
            "sound_velocity": None,
            "altitude_offset": None,
            "correct_for_pitch": None
        }

    class _GeocoderSettings():

        default_settings = {
            "channel": None,
            "imagery": None,
            "anti_alias": None,
            "gain": None,
            "tvg": None,
            "avg": None,
            "avg_window_size": None,
            "despeckle": None,
            "beam_pattern": None,
            "beam_pattern_file": None,
            "nadir_angle": None,
            "filter": None,
            "surface": None,
            "smooth_gyro": None
        }

    _option_registry = {
        'SIPS_BACKSCATTER': _SIPSBackscatterSettings,
        'SIPS_BACKSCATTER_WMA_AREA_AVG': _SIPSBackscatterWMAAreaAvgSettings,
        'SIPS_SIDESCAN': _SIPSSideScanSettings,
        'GEOCODER': _GeocoderSettings,
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Detect HIPS Critical Soundings
class DetectHIPSCriticalSoundings(CarisBatchCommand):
    """
    The DetectHIPSCriticalSoundings class is used to identify Shoalest/Deepest soundings from a HIPS data source based on contour analysis.

    Attributes:
        _command (str): The command associated with the 'Detect HIPS Critical Soundings' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _option_key = 'surface'
    _command = 'DetectHIPSCriticalSoundings'

    _common_settings = {
        "surface": None,
        "input_band": None,
        "output_shoal_status": None,
        "output_deep_status": None,
        "shoal_attributes": None,
        "deep_attributes": None,
        "contour_interval_type": None,
        "max_isolations": None,
        "radius_filter": None
    }

    class _UserIntervalSettings():
        default_settings = {
            "interval": None
        }

    class _LevelsFileSettings():
        default_settings = {
            "contour_levels_file": None
        }

    class _RadiusValueSettings():
        default_settings = {
            "radius_value": None
        }

    class _RadiusTableSettings():
        default_settings = {
            "radius_table_file": None
        }

    _option_registry = {
        'USER_INTERVAL': _UserIntervalSettings,
        'LEVELS_FILE': _LevelsFileSettings,
        'RADIUS_VALUE': _RadiusValueSettings,
        'RADIUS_TABLE': _RadiusTableSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export HIPS
class ExportHIPS(CarisBatchCommand):
    """
    The ExportHIPS class is used to export HIPS data to a supported format.

    Attributes:
        _command (str): The command associated with the 'Export HIPS' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _option_key = 'output_format'
    _command = 'ExportHIPS'

    _common_settings = {
        "output_format": None,
        "single_file": None,
        "overwrite": None,
        "nadir_depth_only": None,
        "include_flag": None,
        "include_header": None,
        "delimiter": None,
        "output_crs": None,
        "coordinate_format": None,
        "coordinate_precision": None,
        "include_attribute": None,
        "z_axis_convention": None,
        "attribute_filter": None,
        "sample": None,
        "elevation_unit": None,
        "coordinate_unit": None,
        "other_precision": None,
        "other_unit": None,
        "ignore_disabled_beams": None
    }

    class _ASCIIOptions():
        default_settings = {
            "single_file": None,
            "overwrite": None,
            "nadir_depth_only": None,
            "include_flag": None,
            "include_header": None,
            "delimiter": None,
            "output_crs": None,
            "coordinate_format": None,
            "coordinate_precision": None,
            "include_attribute": None,
            "z_axis_convention": None,
            "attribute_filter": None,
            "sample": None,
            "elevation_unit": None,
            "coordinate_unit": None,
            "other_precision": None,
            "other_unit": None
        }

    class _GSFOptions():
        default_settings = {
            "ignore_disabled_beams": None
        }

    _option_registry = {
        'ASCII': _ASCIIOptions,
        'GSF': _GSFOptions
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter HIPS Attitude
class FilterHIPSAttitude(CarisBatchCommand):
    """
    The FilterHIPSAttitude class is used for attitude filtering in HIPS data, automatically processing line by line.

    Attributes:
        _command (str): The command associated with the 'Filter HIPS Attitude' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _option_key = 'sensor_type'
    _command = 'FilterHIPSAttitude'

    _common_settings = {
        "sensor_type": None,
        "enable_filtering": None,
        "enable_smoothing": None,
        "filter_break_interpolation": None,
        "filter_type": None,
        "window_size_type": None,
        "threshold": None,
        "window_size_time": None,
        "window_size_sample": None,
    }

    class _SecondsWindowSizeSettings():
        default_settings = {
            "window_size_time": None
        }

    class _PointsWindowSizeSettings():
        default_settings = {
            "window_size_sample": None
        }

    _option_registry = {
        'SECONDS': _SecondsWindowSizeSettings,
        'POINTS': _PointsWindowSizeSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter Observed Depths
class FilterObservedDepths(CarisBatchCommand):
    """
    The FilterObservedDepths class is used for line by line, automatic filtering of the bathymetry in the HIPS data.

    Attributes:
        _command (str): The command associated with the 'Filter Observed Depths' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FilterObservedDepths'
    _option_key = 'bathymetry_type'

    _common_settings = {
        "bathymetry_type": None,
        "accept_data": None,
        "protective_radius": None,
        "protective_radius_designated": None,
        "protective_radius_examined": None,
        "protective_radius_outstanding": None,
        "iho_order": None,
        "iho_limits": None,
        "iho_horizontal_distance_limits": None,
        "filter": None
    }

    class _SWATHSettings:
        """
        Nested class for SWATH-specific settings. 
        """
        default_settings = {
            "b2b_slope_across_track_angle": None,
            "b2b_slope_include_rejected": None,
            "across_track_distance": None,
            "across_track_distance_multiplier": None,
            "beam_numbers": None,
            "nadir_angle": None,
            "reject_quality": None,
            "missing_port_starboard": None,
            "missing_fore_aft": None,
            "missing_any_2_of_4": None
        }

    class _SINGLEBEAMSettings:
        """
        Nested class for SINGLEBEAM-specific settings.
        """
        default_settings = {
            "primary": None,
            "secondary": None,
            "selected": None,
            "b2b_slope_along_track_angle": None,
            "b2b_slope_include_rejected": None,
            "moving_average": None,
            "window_size_type": None,
            "threshold": None
        }

    _option_registry = {
        'SWATH': _SWATHSettings,
        'SINGLEBEAM': _SINGLEBEAMSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter Processed Depths
class FilterProcessedDepths(CarisBatchCommand):
    """
    The FilterProcessedDepths class is used to filter HIPS data with a surface, a polygon or noise confidence values.

    Attributes:
        _command (str): The command associated with the 'Filter Processed Depths' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FilterProcessedDepths'
    _option_key = 'filter_type'

    _common_settings = {
        "filter_type": None,
        "protective_radius": None,
        "protective_radius_designated": None,
        "protective_radius_examined": None,
        "protective_radius_outstanding": None,
        "include_rejected": None
    }

    class _SurfaceSettings:
        """
        Nested class for Surface-specific settings.
        """
        default_settings = {
            "surface": None,
            "threshold_type": None,
            "threshold": None,
            "reject_no_data_soundings": None
        }

    class _PolygonSettings:
        """
        Nested class for Polygon-specific settings.
        """
        default_settings = {
            "geometry": None,
            "extract_type": None,
            "accept_data": None
        }

    class _NoiseConfidenceSettings:
        """
        Nested class for Noise Confidence-specific settings.
        """
        default_settings = {
            "threshold": None
        }

    _option_registry = {
        'SURFACE': _SurfaceSettings,
        'POLYGON': _PolygonSettings,
        'NOISE_CONFIDENCE': _NoiseConfidenceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Georeference Bathymetry
class GeoreferenceHIPSBathymetry(CarisBatchCommand):
    """
    The GeoreferenceHIPSBathymetry class is used to georeference bathymetry data in HIPS using various options such as 
    ray tracing, tidal adjustments, and uncertainty calculations.

    Attributes:
        _command (str): The command associated with the 'Georeference HIPSBathymetry' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'GeoreferenceHIPSBathymetry'
    _option_key = None

    _common_settings = {
        "compute_svc": None,
        "svp": None,
        "ssp_as_backup_svp": None,
        "profile_selection_method": None,
        "nearest_distance_hours": None,
        "ssp": None,
        "resteer_beam_angles": None,
        "source_heave": None,
        "vehicle_depth": None,
        "compute_tpu": None,
        "tide_measured": None,
        "tide_zoning": None,
        "source_gps_height": None,
        "gps_sounding_datum": None,
        "sv_measured": None,
        "sv_surface": None,
        "sweep_max_heave": None,
        "sweep_max_pitch": None,
        "sweep_max_roll": None,
        "source_sonar": None,
        "source_navigation": None,
        "source_gyro": None,
        "source_pitch": None,
        "source_roll": None,
        "source_heave": None,
        "source_tide": None,
        "vertical_datum_reference": None,
        "tide_file": None,
        "weighted_average": None,
        "compute_errors": None,
        "compute_gps_vertical_adjustment": None,
        "smooth_height": None,
        "sounding_datum_offset": None,
        "datum_model_file": None,
        "datum_model_band": None,
        "info_file": None,
        "input_crs": None,
        "output_components": None,
        "gps_vertical_components": None,
        "gps_component_antenna_offset": None,
        "gps_component_dynamic_heave": None,
        "gps_component_mru_remote_heave": None,
        "gps_component_dynamic_draft": None,
        "gps_component_vehicle_depth": None,
        "gps_component_waterline": None,
        "vertical_offset": None,
        "apply_refraction_coeff": None,
        "beam_shift": None,
        "beam_shift_file": None,
        "smooth_sensor": None
    }

    class _GeoreferenceSettings:
        """
        Nested class for GeoreferenceHIPSBathymetry settings. 
        """
        default_settings = {}

    _option_registry = {
        'GEOREFERENCEHIPSBATHYMETRY': _GeoreferenceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import Generic To HIPS
class ImportGenericToHIPS:
    """
    The ImportGenericToHIPS class is used to convert ASCII data files into HIPS format using a parser configuration file.

    Attributes:
        _command (str): The command associated with the 'Import Generic To HIPS' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportGenericToHIPS'
    _option_key = None

    _common_settings = {
        "parser_file": None,
        "input_crs": None,
        "vessel_file": None,
        "extent": None,
        "filter": None,
        "filter_dup_navigation": None
    }

    class _ImportGenericSettings:
        """
        Nested class for ImportGenericToHIPS settings.
        """
        default_settings = {}

    _option_registry = {
        'IMPORTGENERICTOHIPS': _ImportGenericSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import HIPS From Auxiliary
class ImportHIPSFromAuxiliary:
    """
    The ImportHIPSFromAuxiliary class is used to import various post-processed formats into HIPS and SIPS projects.

    Attributes:
        _command (str): The command associated with the 'Import HIPS From Auxiliary' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportHIPSFromAuxiliary'
    _option_key = 'input_format'

    _common_settings = {
        "input_format": None,
        "time_offset": None,
        "time_buffer": None,
        "maximum_gap": None,
        "allow_partial": None
    }

    class _AsciiSettings:
        default_settings = {
            "input_crs": None,
            "navigation": None,
            "gps_height": None,
            "info_file": None
        }

    class _PosMvSettings:
        default_settings = {
            "input_crs": None,
            "navigation": None,
            "gyro": None,
            "pitch": None,
            "roll": None,
            "gps_height": None,
            "delayed_heave": None,
            "navigation_rms": None,
            "gyro_rms": None,
            "pitch_rms": None,
            "roll_rms": None,
            "delayed_heave_rms": None,
            "gps_height_rms": None,
            "heave_rms": None,
            "reference_week": None
        }

    class _RMSSettings:
        default_settings = {
            "navigation_rms": None,
            "gyro_rms": None,
            "pitch_rms": None,
            "roll_rms": None,
            "gps_height_rms": None,
            "reference_week": None
        }

    class _SBETSettings:
        default_settings = {
            "input_crs": None,
            "navigation": None,
            "gyro": None,
            "pitch": None,
            "roll": None,
            "gps_height": None,
            "reference_week": None
        }

    class _NavlabSettings:
        default_settings = {
            "input_crs": None,
            "navigation": None,
            "gyro": None,
            "pitch": None,
            "roll": None,
            "subsea_depth": None,
            "navigation_rms": None,
            "gyro_rms": None,
            "pitch_rms": None,
            "roll_rms": None,
            "subsea_depth_rms": None
        }

    class _NovatelSettings:
        default_settings = {
            "input_crs": None,
            "navigation": None,
            "gyro": None,
            "pitch": None,
            "roll": None,
            "gps_height": None,
            "delayed_heave": None,
            "navigation_rms": None,
            "gyro_rms": None,
            "pitch_rms": None,
            "roll_rms": None,
            "gps_height_rms": None
        }

    class _PFreeHeaveSettings:
        default_settings = {
            "delayed_heave": None
        }

    class _StarfixSettings:
        default_settings = {
            "navigation": None,
            "gyro": None,
            "pitch": None,
            "roll": None,
            "gps_height": None,
            "delayed_heave": None,
            "subsea_depth": None,
            "input_crs": None,
            "vessel_name": None,
            "navigation_device": None,
            "heading_device": None,
            "heave_device": None,
            "motion_device": None,
            "subsea_depth_device": None
        }

    class _TerraModelSettings:
        default_settings = {
            "input_crs": None,
            "navigation": None,
            "gps_height": None,
            "navigation_rms": None,
            "gps_height_rms": None
        }

    _option_registry = {
        'ASCII': _AsciiSettings,
        'APP_POSMV': _PosMvSettings,
        'APP_RMS': _RMSSettings,
        'APP_SBET': _SBETSettings,
        'NAVLAB': _NavlabSettings,
        'NOVATEL': _NovatelSettings,
        'PFREEHEAVE': _PFreeHeaveSettings,
        'STARFIX': _StarfixSettings,
        'TERRAPOS': _TerraModelSettings,
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import Kraken TIL To Mosaic
class ImportKrakenTILToMosaic:
    """
    The ImportKrakenTILToMosaic class is used to create a raster mosaic from one or more Kraken .TIL files.

    Attributes:
        _command (str): The command associated with the 'Import Kraken TIL To Mosaic' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportKrakenTILToMosaic'
    _option_key = None

    _common_settings = {
        "resolution": None,
        "output_crs": None,
        "extent": None
    }

    class _ImportKrakenTILToMosaicSettings:
        """
        Nested class for ImportKrakenTILToMosaic settings.
        """
        default_settings = {}

    _option_registry = {
        'IMPORTKRAKENTILTOMOSAIC': _ImportKrakenTILToMosaicSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import Multiple Detections To HIPS
class ImportMultipleDetectionsToHIPS:
    """
    The ImportMultipleDetectionsToHIPS class is used to import additional bottom detections per beam for use in HIPS processes.

    Attributes:
        _command (str): The command associated with the 'Import Multiple Detections To HIPS' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportMultipleDetectionsToHIPS'
    _option_key = None

    _common_settings = {
        "reject_type": None
    }

    class _ImportMultipleDetectionsToHIPSSettings:
        """
        Nested class for ImportMultipleDetectionsToHIPS settings.
        """
        default_settings = {}

    _option_registry = {
        'IMPORTMULTIPLEDETECTIONSTOHIPS': _ImportMultipleDetectionsToHIPSSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import Tide To HIPS
class ImportTideToHIPS:
    """
    The ImportTideToHIPS class is used to apply tidal observation data to HIPS track lines.

    Attributes:
        _command (str): The command associated with the 'Import Tide To HIPS' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportTideToHIPS'
    _option_key = 'interpolation_type'

    _common_settings = {
        "interpolation_type": None,
        "tide_file": None
    }

    class _SingleStationSettings:
        """
        Nested class for Single-Station settings in ImportTideToHIPS.
        """
        default_settings = {}

    class _MultiStationSettings:
        """
        Nested class for Multi-Station settings in ImportTideToHIPS.
        """
        default_settings = {
            "weighted_average": None,
            "compute_errors": None
        }

    _option_registry = {
        'MULTI_STATION': _MultiStationSettings,
        'SINGLE_STATION': _SingleStationSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Import To HIPS
class ImportToHIPS(CarisBatchCommand):
    """
    The ImportToHIPS class is used to import various formats to HIPS and SIPS.

    Attributes:
        _command (str): The command associated with the 'Import To HIPS' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportToHIPS'
    _option_key = 'input_format'

    _common_settings = {
        "input_format": None,
        "input_crs": None,
        "carry_raw_data_files": None,
        "vessel_file": None,
        "extract_svp": None,
        "overwrite": None,
        "filter_extent_type": None,
        "extent": None,
        "filter": None,
        "filter_amplitude_percent": None,
        "filter_angle_1": None,
        "filter_angle_2": None,
        "filter_range": None,
        "filter_across_track_distance": None,
        "filter_depth_multiplier": None,
        "filter_stat_threshold": None,
        "filter_stat_sector_angle": None,
        "filter_stat_bin_size": None,
        "filter_stat_thin_factor": None,
        "filter_stat_depth_comparator": None,
        "filter_keep_thinned_data": None
    }

    class _AtlasASDSettings():

        default_settings = {
            "convert_side_scan": None
        }

    class _AtlasHydrosweepSettings():

        default_settings = {
            "survey_year": None
        }

    class _AtlasSurfSettings():

        default_settings = {
            "convert_side_scan": None,
            "convert_bathymetry": None,
            "use_higher_frequency": None
        }

    class _BathyswathSXRSettings():

        default_settings = {
            "sound_velocity": None
        }

    class _BathyswathSXISettings():

        default_settings = {}

    class _BathyswathSXPSettings():

        default_settings = {}

    class _Chirpscan3DSettings():

        default_settings = {}

    class _CMAXSettings():

        default_settings = {
            "survey_date": None
        }

    class _CodaSettings():

        default_settings = {
            "cable_out_is_layback": None,
            "sonar_channel": None
        }

    class _Edgetech260Settings():

        default_settings = {
            "survey_date": None
        }

    class _EdgetechJSFSettings():

        default_settings = {
            "convert_side_scan": None,
            "convert_from_cable_out": None,
            "sensor_depth_location": None,
            "sensor_altitude_location": None,
            "convert_bathymetry": None,
            "output_filtered_data": None,
            "echo_strength_percent": None,
            "quality_percent": None,
            "snr_db": None
        }

    class _EdgetechMidasSettings():

        default_settings = {
            "convert_side_scan": None
        }

    class _EIVASBDSettings():

        default_settings = {
            "convert_side_scan": None,
            "depth_source": None,
            "navigation_device": None,
            "heading_device": None,
            "motion_device": None,
            "convert_vehicle_depth": None,
            "pad_with_null": None,
            "swap_transducers": None,
            "separate_dual_head_data": None
        }

    class _ELACXSESettings():

        default_settings = {
            "attitude_source": None,
            "surface_sound_speed": None,
            "convert_side_sca": None,
            "stbd_to_port_numbering": None,
            "pad_with_null": None
        }

    class _FAUSettings():

        default_settings = {
            "roll_angle_multiplier": None,
            "beam_setting": None
        }

    class _FurunoLOGSettings():

        default_settings = {
            "convert_side_scan": None
        }

    class _GeoAcousticsRDFSettings():

        default_settings = {
            "convert_side_scan": None,
            "convert_vehicle_depth": None,
            "filter_water_column": None,
            "filter_post_processing": None
        }

    class _GeoAcousticsRFFSettings():

        default_settings = {
            "convert_vehicle_depth": None,
            "filter_acquisition": None,
            "filter_post_processing": None
        }

    class _GenericSensorFormatSettings():

        default_settings = {
            "depth_source": None,
            "include_offline": None,
            "reject_offline": None
        }

    class _HawkeyeBINSettings():

        default_settings = {
            "depth_source": None,
            "import_type": None,
            "invalid_as_positive_99": None
        }

    class _HypackSettings():

        default_settings = {
            "sound_velocity": None,
            "convert_bathymetry": None,
            "convert_side_scan": None,
            "apply_static_draft": None,
            "navigation_device": None,
            "heading_device": None,
            "motion_device": None,
            "port_device": None,
            "stbd_device": None,
            "sow_device": None,
            "ss_postion_device": None,
            "hours_from_gmt": None,
            "convert_from_cable_out": None
        }

    class _HypackHS2Settings():

        default_settings = {
            "survey_date": None,
            "depths_in_feet": None
        }

    class _ImagenexSettings():

        default_settings = {
            "gps_string_type": None
        }

    class _KleinSDFSettings():

        default_settings = {
            "convert_side_scan": None,
            "include_hidden": None,
            "convert_sss_gyro": None,
            "convert_aux_altitude": None,
            "pressure_sensor_psi": None,
            "pressure_sensor_range": None,
            "cable_out_is_layback": None,
            "convert_aux_depth": None,
            "convert_vehicle_depth": None,
            "convert_bathymetry": None,
            "snr_filter": None,
            "uncertainty_filter": None,
            "confidence_value": None,
            "output_filtered_data": None,
            "heave_positive_down": None,
            "pitch_positive_bow_up": None,
            "roll_positive_port_up": None,
            "yaw_ccw_from_north": None
        }

    class _KongsbergKMALLSettings():

        default_settings = {
            "convert_navigation": None,
            "navigation_device": None,
            "gps_timestamps": None,
            "gps_height_device": None,
            "heading_device": None,
            "heave_device": None,
            "pitch_device": None,
            "roll_device": None,
            "delayed_heave_device": None,
            "convert_vehicle_depth": None,
            "time_shift": None
        }

    class _KongsbergALLSettings():

        default_settings = {
            "convert_navigation": None,
            "navigation_device": None,
            "gps_height_device": None,
            "gps_time_stamps": None,
            "heading_device": None,
            "heave_device": None,
            "pitch_device": None,
            "roll_device": None,
            "ssp_device": None,
            "convert_vehicle_depth": None,
            "time_shift": None
        }

    class _KongsbergEA600Settings():

        default_settings = {
            "convert_bathymetry": None,
            "port_device": None,
            "stbd_device": None,
        }

    class _KrakenSettings():

        default_settings = {}

    class _LadsCAFSettings():

        default_settings = {}

    class _LASSettings():

        default_settings = {
            "invert_elevation": None,
            "override_date": None,
            "survey_date": None,
            "override_crs": None,
            "flag_synthetic": None,
            "flag_key_point": None,
            "flag_overlap": None,
            "flag_withheld": None
        }

    class _MarineSonicsSettings():

        default_settings = {}

    class _ProsasSettings():

        default_settings = {
            "convert_q0_data": None
        }

    class _QMIPSSettings():

        default_settings = {
            "use_alt_channel": None
        }

    class _ScrippsSettings():

        default_settings = {}

    class _SeabeamSettings():

        default_settings = {
            "convert_side_scan": None,
            "convert_vehicle_depth": None
        }

    class _SEGYSettings():

        default_settings = {}

    class _ShoalsSettings():

        default_settings = {
            "confidence_value": None,
            "tof_convert": None
        }

    class _SonardyneSettings():

        default_settings = {}

    class _SPAWARSettings():

        default_settings = {}

    class _TeledyneTDYSettings():

        default_settings = {}

    class _TeledyneS7KSettings():

        default_settings = {
            "convert_bathymetry": None,
            "separate_dual": None,
            "reject_quality": None,
            "navigation_device": None,
            "heading_device": None,
            "motion_device": None,
            "swath_device": None,
            "convert_vehicle_depth": None
        }

    class _TeledynePDSSettings():

        default_settings = {
            "convert_bathymetry": None,
            "include_offline": None,
            "reject_quality": None,
            "navigation_device": None,
            "heading_device": None,
            "motion_device": None,
            "source_type": None,
            "device_number": None,
            "primary_channel": None,
            "secondary_channe": None
        }

    class _UNBSettings():

        default_settings = {
            "is_dual_head": None,
            "convert_backscatter": None
        }

    class _WinfrogSettings():

        default_settings = {
            "convert_bathymetry": None,
            "navigation_device": None,
            "motion_device": None,
            "sound_velocity": None
        }

    class _XTFSettings():
        default_settings = {
            "navigation_device": None,
            "gps_height_device": None,
            "motion_device": None,
            "convert_bathymetry": None,
            "heading_device": None,
            "reject_quality": None,
            "convert_side_scan": None,
            "ss_weighting_factor": None,
            "ss_navigation_device": None,
            "ss_heading_device": None,
            "include_offline": None,
            "convert_layback_cable_out": None,
            "layback_multiplier": None,
            "use_aux_value": None,
            "convert_vehicle_depth": None,
            "timestamps": None,
            "use_time_sync": None
        }

    _option_registry = {
        "ATLAS_ASD": _AtlasASDSettings,
        "ATLAS_HYDROSWEEPDS": _AtlasHydrosweepSettings,
        "ATLAS_SURF": _AtlasSurfSettings,
        "BATHYSWATH_SXR": _BathyswathSXRSettings,
        "BATHYSWATH_SXI": _BathyswathSXISettings,
        "BATHYSWATH_SXP": _BathyswathSXPSettings,
        "CHIRPSCAN3D": _Chirpscan3DSettings,
        "CMAX": _CMAXSettings,
        "CODA": _CodaSettings,
        "EDGETECH_260": _Edgetech260Settings,
        "EDGETECH_JSF": _EdgetechJSFSettings,
        "EDGETECH_MIDAS": _EdgetechMidasSettings,
        "EIVA": _EIVASBDSettings,
        "ELAC": _ELACXSESettings,
        "FAU": _FAUSettings,
        "FURUNO": _FurunoLOGSettings,
        "GEOACOUSTICS_RDF": _GeoAcousticsRDFSettings,
        "GEOACOUSTICS_RFF": _GeoAcousticsRFFSettings,
        "GSF": _GenericSensorFormatSettings,
        "HAWKEYE": _HawkeyeBINSettings,
        "HYPACK": _HypackSettings,
        "HYPACK_HS2": _HypackHS2Settings,
        "IMAGENEX": _ImagenexSettings,
        "KLEIN": _KleinSDFSettings,
        "KONGSBERGKMALL": _KongsbergKMALLSettings,
        "KONGSBERG": _KongsbergALLSettings,
        "KONGSBERG_EA600": _KongsbergEA600Settings,
        "KRAKEN": _KrakenSettings,
        "LADS": _LadsCAFSettings,
        "LAS": _LASSettings,
        "MARINESONICS": _MarineSonicsSettings,
        "PROSAS": _ProsasSettings,
        "QMIPS": _QMIPSSettings,
        "SCRIPPS": _ScrippsSettings,
        "SEABEAM": _SeabeamSettings,
        "SEGY": _SEGYSettings,
        "SHOALS": _ShoalsSettings,
        "SONARDYNE": _SonardyneSettings,
        "SPAWAR": _SPAWARSettings,
        "TELEDYNE": _TeledyneTDYSettings,
        "TELEDYNE7K": _TeledyneS7KSettings,
        "TELEDYNE_PDS": _TeledynePDSSettings,
        "UNB": _UNBSettings,
        "WINFROG": _WinfrogSettings,
        "XTF": _XTFSettings,
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Move HIPS to HIPS
class MoveHIPSToHIPS(CarisBatchCommand):
    """
    The MoveHIPSToHIPS class is used to move HIPS track lines from one HIPS file to another. 
    This class manages the command and options specific to this process.

    Attributes:
        _command (str): The command associated with the 'Move HIPS to HIPS' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'MoveHIPSToHIPS'
    _option_key = None

    _common_settings = {
        "carry_over": None
    }

    class _MoveHIPSToHIPSSettings:
        """
        Nested class for MoveHIPSToHIPS settings. 
        """
        default_settings = {}

    _option_registry = {
        'MOVEHIPSTOHIPS': _MoveHIPSToHIPSSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Recompute HIPS Grid
class RecomputeHIPSGrid(CarisBatchCommand):
    """
    The RecomputeHIPSGrid class is used to re-grid all HIPS sources from an existing surface. 
    This process utilizes the create process parameters stored in the CSAR metadata.

    Attributes:
        _command (str): The command associated with the 'Recompute HIPS Grid' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RecomputeHIPSGrid'
    _option_key = None

    _common_settings = {
        # No specific settings are needed as per the process description.
    }

    class _RecomputeHIPSGridSettings:
        """
        Nested class for RecomputeHIPSGrid settings. 
        """
        default_settings = {}

    _option_registry = {
        'RECOMPUTEHIPSGRID': _RecomputeHIPSGridSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Remove From HIPS Grid
class RemoveFromHIPSGrid(CarisBatchCommand):
    """
    The RemoveFromHIPSGrid class is used to remove HIPS track lines from an existing HIPS surface.
    This process utilizes the process parameters stored in the CSAR metadata.

    Attributes:
        _command (str): The command associated with the 'Remove from HIPS Grid' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RemoveFromHIPSGrid'
    _option_key = None

    _common_settings = {
        # No specific settings are needed as per the process description.
    }

    class _RemoveFromHIPSGridSettings:
        """
        Nested class for RemoveFromHIPSGrid settings. 
        """
        default_settings = {}

    _option_registry = {
        'REMOVEFROMHIPSGRID': _RemoveFromHIPSGridSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Remove From SIPS Mosaic
class RemoveFromSIPSMosaic(CarisBatchCommand):
    """
    The RemoveFromSIPSMosaic class is used to remove HIPS sources from an existing SIPS mosaic.
    This process utilizes the create process parameters stored in the CSAR metadata.

    Attributes:
        _command (str): The command associated with the 'Remove from SIPS Mosaic' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RemoveFromSIPSMosaic'
    _option_key = None

    _common_settings = {
        # No specific settings are needed as per the process description.
    }

    class _RemoveFromSIPSMosaicSettings:
        """
        Nested class for RemoveFromSIPSMosaic settings. 
        """
        default_settings = {}

    _option_registry = {
        'REMOVEFROMSIPSMOSAIC': _RemoveFromSIPSMosaicSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Reset HIPS Status
class ResetHIPSStatus(CarisBatchCommand):
    """
    The ResetHIPSStatus class is used to reset the status of all HIPS data specified in the process to Accepted.

    Attributes:
        _command (str): The command associated with the 'Reset HIPS Status' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ResetHIPSStatus'
    _option_key = None

    _common_settings = {
        "status": None
    }

    class _ResetHIPSStatusSettings:
        """
        Nested class for ResetHIPSStatus settings. 
        """
        default_settings = {}

    _option_registry = {
        'RESETHIPSSTATUS': _ResetHIPSStatusSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Set HIPS Navigation Source
class SetHIPSNavigationSource(CarisBatchCommand):
    """
    The SetHIPSNavigationSource class changes the source of navigation datagrams used by HIPS track lines.

    Attributes:
        _command (str): The command associated with the 'Set HIPS Navigation Source' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'SetHIPSNavigationSource'
    _option_key = None

    _common_settings = {
        "source": None,
        "type": None
    }

    class _SetHIPSNavigationSourceSettings:
        """
        Nested class for SetHIPSNavigationSource settings.
        """
        default_settings = {}

    _option_registry = {
        'SETHIPSNAVIGATIONSOURCE': _SetHIPSNavigationSourceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Shift HIPS Navigation
class ShiftHIPSNavigation(CarisBatchCommand):
    """
    The ShiftHIPSNavigation class is used to shift the HIPS data track line navigation by a specified amount.
    This process updates the HIPS track lines and the associated project file.

    Attributes:
        _command (str): The command associated with the 'Shift Navigation' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ShiftHIPSNavigation'
    _option_key = None

    _common_settings = {
        "shift": None
    }

    class _ShiftHIPSNavigationSettings:
        """
        Nested class for ShiftHIPSNavigation settings.
        """
        default_settings = {}

    _option_registry = {
        'SHIFTHIPSNAVIGATION': _ShiftHIPSNavigationSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Sound Velocity Correct HIPS (Kongsberg)
class SoundVelocityCorrectHIPS(CarisBatchCommand):
    """
    The SoundVelocityCorrectHIPS class applies sound velocity profiles using a ray tracing algorithm to HIPS track lines.
    This process corrects the depths for sound velocity and updates the HIPS track lines accordingly.

    Attributes:
        _command (str): The command associated with the 'Sound Velocity Correction (using Kongsberg Library)' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'SoundVelocityCorrectHIPS'
    _option_key = 'algorithm'

    _common_settings = {
        "algorithm": None,
        "svp_file": None,
        "profile_selection_method": None,
        "heave_source": None,
        "smooth_sensor": None,
        "nearest_distance_hours": None,
        "resteer_beam_angles": None
    }

    class _SoundVelocityCorrectHIPS_Caris:
        """
        Nested class for SoundVelocityCorrectHIPS settings specific to the CARIS algorithm.
        """
        default_settings = {
            "ssp": None,
            "svc_line": None
        }

    class _SoundVelocityCorrectHIPS_KongsbergLibrary:
        """
        Nested class for SoundVelocityCorrectHIPS settings specific to the KONGSBERG_LIBRARY algorithm.
        """
        default_settings = {
            # No additional settings specific to KONGSBERG_LIBRARY
        }

    _option_registry = {
        'CARIS': _SoundVelocityCorrectHIPS_Caris,
        'KONGSBERG_LIBRARY': _SoundVelocityCorrectHIPS_KongsbergLibrary
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update HIPS Additional Bathymetry
class UpdateHIPSAdditionalBathymetry(CarisBatchCommand):
    """
    The UpdateHIPSAdditionalBathymetry class updates stored additional bathymetry in a HIPS project. 
    This process is typically used when corrections like tide or sound velocity profiles (SVP) have been applied 
    and require the Merge process to be re-applied.

    Attributes:
        _command (str): The command associated with the 'Update HIPS Additional Bathymetry' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateHIPSAdditionalBathymetry'
    _option_key = None

    _common_settings = {
        # No specific settings are needed as per the process description.
    }

    class _UpdateHIPSAdditionalBathymetrySettings:
        """
        Nested class for UpdateHIPSAdditionalBathymetry settings.
        """
        default_settings = {}

    _option_registry = {
        'UPDATEHIPSADDITIONALBATHYMETRY': _UpdateHIPSAdditionalBathymetrySettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update Raster CUBE Disambiguation
class UpdateRasterCUBEDisambiguation(CarisBatchCommand):
    """
    The UpdateRasterCUBEDisambiguation class is used to change the disambiguation method 
    used in CUBE surfaces within a HIPS project.

    Attributes:
        _command (str): The command associated with the 'Update Raster CUBE Disambiguation' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateRasterCUBEDisambiguation'
    _option_key = None

    _common_settings = {
        "disambiguation_method": None
    }

    class _UpdateRasterCUBEDisambiguationSettings:
        """
        Nested class for UpdateRasterCUBEDisambiguation settings.
        """
        default_settings = {
            # No specific settings are needed as per the process description.
        }

    _option_registry = {
        'UPDATERASTERCUBEDISAMBIGUATION': _UpdateRasterCUBEDisambiguationSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update SIPS Contact Positions
class UpdateSIPSContactPositions(CarisBatchCommand):
    """
    The UpdateSIPSContactPositions class is used to recompute all contacts in specified HIPS track lines.

    Attributes:
        _command (str): The command associated with the 'Update SIPS Contact Positions' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateSIPSContactPositions'
    _option_key = None

    _common_settings = {
        # No specific settings are needed as per the process description.
    }

    class _UpdateSIPSContactPositionsSettings:
        """
        Nested class for UpdateSIPSContactPositions settings. 
        """
        default_settings = {}

    _option_registry = {
        'UPDATESIPSCONTACTPOSITIONS': _UpdateSIPSContactPositionsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update SVP Positions
class UpdateSVPPositions(CarisBatchCommand):
    """
    The UpdateSVPPositions class is used to analyze and update sound velocity profiles (SVP) 
    with position values using positions from HIPS and SIPS track lines.

    Attributes:
        _command (str): The command associated with the 'Update SVP Positions' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateSVPPositions'
    _option_key = None

    _common_settings = {
        "svp": None
    }

    class _UpdateSVPPositionsSettings:
        """
        Nested class for UpdateSVPPositions settings.
        """
        default_settings = {}

    _option_registry = {
        'UPDATESVPPOSITIONS': _UpdateSVPPositionsSettings
    }
