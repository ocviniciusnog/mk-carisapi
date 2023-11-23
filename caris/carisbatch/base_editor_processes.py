"""
Base Editor Processes Module

This module extends the CarisBatchCommand class to provide a comprehensive suite
of raster and vector data manipulation functionalities. It includes classes for
various operations such as adding computed bands, modifying raster headers,
exporting products, and more, each designed for specific tasks in a geospatial
data processing workflow.

The classes encapsulate commands and parameters for a wide range of processes, 
from simple raster modifications to complex vector data transformations. These 
classes facilitate efficient data processing, ensuring accuracy and consistency 
in operations.

Author: Vinicius Nogueira
Created: 15-July-2020
Last Modified: 23-November-2023

Note:
    This module is an integral part of the MK-CarisAPI.
"""

from ._carisbatch import CarisBatchCommand

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add Computed Band Description
class AddComputedBand(CarisBatchCommand):
    """
    The AddComputedBand class is used to add a computed band to an existing coverage by applying a numeric expression to the existing data.

    Attributes:
        _command (str): The command associated with the 'Add Computed Band' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddComputedBand'
    _option_key = None

    _common_settings = {
        "compute_band": None,
        "expression": None,
        "expression_file": None,
        "z_axis_convention": None,
        "computed_band_type": None
    }
    
    class _AddComputedBandSettings:
        """
        Nested class for AddComputedBand settings. 
        """
        default_settings = {}
        
    _option_registry = {
        'ADDCOMPUTEDBAND': _AddComputedBandSettings
    }
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add Empty Band
class AddEmptyBand(CarisBatchCommand):
    """
    The AddEmptyBand class is used to create a new band with no data values at every node in a coverage. This process is often used in conjunction with the UpdateBandValues process to create and populate a new permanent band in a coverage.

    Attributes:
        _command (str): The command associated with the 'Add Empty Band' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddEmptyBand'
    _option_key = None

    _common_settings = {
        "category": None,
        "band_name": None,
        "unit": None,
        "direction_type": None,
        "numeric_type": None
    }
    
    class _AddEmptyBandSettings:
        """
        Nested class for AddEmptyBand settings. 
        """
        default_settings = {}
        
    _option_registry = {
        'ADDEMPTYBAND': _AddEmptyBandSettings
    }
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add Slope Bands
class AddSlopeBands(CarisBatchCommand):
    """
    The AddSlopeBands class is used to add slope and aspect bands to a raster surface. This process updates a raster surface in CSAR format by adding these bands, but it does not have specific options to configure.

    Attributes:
        _command (str): The command associated with the 'Add Slope Bands' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddSlopeBands'
    _option_key = None

    _common_settings = {}
    
    class _AddSlopeBandsSettings:
        """
        Nested class for AddSlopeBands settings. 
        """
        default_settings = {}
        
    _option_registry = {
        'ADDSLOPEBANDS': _AddSlopeBandsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add Smoothed Band
class AddSmoothedBand(CarisBatchCommand):
    """
    The AddSmoothedBand class is used to add a new smoothed elevation band to an existing coverage using various smoothing methods.

    Attributes:
        _command (str): The command associated with the 'Add Smoothed Band' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddSmoothedBand'
    _option_key = 'method'

    _common_settings = {
        "method": None,
        "input_band": None,
        "smoothed_band": None
    }
    
    class _LaplacianSettings:
        """
        Nested class for Laplacian smoothing settings.
        """
        default_settings = {
            "iterations": 20
        }

    class _RestrainedLaplacianSettings:
        """
        Nested class for Restrained Laplacian smoothing settings.
        """
        default_settings = {
            "iterations": 20
        }

    class _ExpandShoalsSettings:
        """
        Nested class for Expand Shoals smoothing settings.
        """
        default_settings = {
            "radius_type": 'MULTIPLIER',
            "radius": 0.0,
            "multiplier": 5,
            "radius_coefficients": None,
            "isolations_only": False,
            "dropoff_slope": -0.125,
            "scale": 1
        }

    class _ConstrainSlopesSettings:
        """
        Nested class for Constrain Slopes smoothing settings.
        """
        default_settings = {
            "vertical_rise": 10.0,
            "horizontal_run": 10.0,
            "scale": 1
        }

    class _RollingCoinSettings:
        """
        Nested class for Rolling Coin smoothing settings.
        """
        default_settings = {
            "multiplier": 5,
            "radius_coefficients": None
        }
        
    _option_registry = {
        'LAPLACIAN': _LaplacianSettings,
        'RESTRAINED_LAPLACIAN': _RestrainedLaplacianSettings,
        'EXPAND_SHOALS': _ExpandShoalsSettings,
        'CONSTRAIN_SLOPES': _ConstrainSlopesSettings,
        'ROLLING_COIN': _RollingCoinSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add to Raster Combine
class AddToRasterCombine(CarisBatchCommand):
    """
    The AddToRasterCombine class is used to add sources to an existing combined raster using 
    the combine process parameters stored in the CSAR metadata. This is equivalent to 
    performing the original combine process with all of the sources.

    Attributes:
        _command (str): The command associated with the 'Add to Raster Combine' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddToRasterCombine'
    _option_key = None

    _common_settings = {
        "recurse": None
    }

    class _AddToRasterCombineSettings:
        """
        Nested class for AddToRasterCombine settings.
        """
        default_settings = {}
        
    _option_registry = {
        'ADDTORASTERCOMBINE': _AddToRasterCombineSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Classify Points for Cartography
class ClassifyPointsForCartography(CarisBatchCommand):
    """
    The ClassifyPointsForCartography class is used to set values for two bands in a point cloud. 
    It updates a point cloud in CSAR format, adding or updating the "Selection State" and "Selection Rule" bands.

    Attributes:
        _command (str): The command associated with the 'Classify Points for Cartography' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ClassifyPointsForCartography'
    _option_key = 'method'

    _common_settings = {
        "method": None,
        "input_band": None,
        "feature_catalogue": None,
        "rule_name": None,
        # Additional common options can be added here.
    }

    class _SuppressionSettings:
        """
        Nested class for Suppression settings.
        """
        default_settings = {
            "area_features": None,
            "elevation_lookup": None,
            "suppression_threshold": None
        }

    class _SelectByBiasSettings:
        """
        Nested class for Select By Bias settings.
        """
        default_settings = {
            "selection_method": None,
            "radius_coefficients": None,
            "scale": None,
            "area_features": None
        }

    class _SelectBasedOnReferenceSettings:
        """
        Nested class for Select Based On Reference settings.
        """
        default_settings = {
            "selection_method": None,
            "reference_features": None,
            "elevation_lookup": None,
            "vertical_tolerance": None,
            "vertical_tolerance_percentage": None,
            "radius_coefficients": None,
            "scale": None,
            "area_features": None
        }

    class _SelectLocalShoalsSettings:
        """
        Nested class for Select Local Shoals settings.
        """
        default_settings = {
            "vertical_tolerance_percentage": None,
            "radius_coefficients": None,
            "scale": None,
            "area_features": None
        }

    class _IsolatedContourSettings:
        """
        Nested class for Isolated Contour settings.
        """
        default_settings = {
            "selection_method": None,
            "contour_features": None,
            "reference_area_features": None,
            "elevation_lookup": None
        }

    class _SelectExtremaInAreasSettings:
        """
        Nested class for Select Extrema In Areas settings.
        """
        default_settings = {
            "selection_method": None,
            "area_features": None
        }

    _option_registry = {
        "SUPPRESSION": _SuppressionSettings,
        "SELECT_BY_BIAS": _SelectByBiasSettings,
        "SELECT_BASED_ON_REFERENCE": _SelectBasedOnReferenceSettings,
        "SELECT_LOCAL_SHOALS": _SelectLocalShoalsSettings,
        "ISOLATED_CONTOUR": _IsolatedContourSettings,
        "SELECT_EXTREMA_IN_AREAS": _SelectExtremaInAreasSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Classify Raster Holidays
class ClassifyRasterHolidays(CarisBatchCommand):
    """
    The ClassifyRasterHolidays class is used to assign each cell in a raster band as valid data, 
    no data, or an interior holiday (hole).

    Attributes:
        _command (str): The command associated with the 'Classify Raster Holidays' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ClassifyRasterHolidays'
    _option_key = None

    _common_settings = {
        "input_band": None,
        "classify_no_data": None
    }

    class _ClassifyRasterHolidaysSettings:
        """
        Nested class for ClassifyRasterHolidays settings.
        """
        default_settings = {}
        
    _option_registry = {
        'CLASSIFYRASTERHOLIDAYS': _ClassifyRasterHolidaysSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Clip Raster
class ClipRaster(CarisBatchCommand):
    """
    The ClipRaster class is used to export a defined portion of the input file.

    Attributes:
        _command (str): The command associated with the 'Clip Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ClipRaster'
    _option_key = None

    _common_settings = {
        "extent": None
    }

    class _ClipRasterSettings:
        """
        Nested class for ClipRaster settings.
        """
        default_settings = {}
        
    _option_registry = {
        'CLIPRASTER': _ClipRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Combine to Raster
class CombineToRaster(CarisBatchCommand):
    """
    The CombineToRaster class creates a new raster by computing the value in each raster cell using a logical 
    operation executed over the points within each raster cell. This is used for combining overlapping coverages 
    or regenerating a coverage using different settings.

    Attributes:
        _command (str): The command associated with the 'Combine to Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CombineToRaster'
    _option_key = None

    _common_settings = {
        "recompute_stats": None,
        "rule_file": None,
        "override_ambiguity": None,
        "confine_metadata_rules": None,
        "recurse": None,
        "use_cell_centres": None,
        "contributor_attribute": None,
        "resolution": None,
        "anchor": None,
        "extent": None,
        "primary_band": None,
        "map_band": None,
        "output_crs": None,
        "output_vertical_crs": None,
        "comments": None
    }

    class _CombineToRasterSettings:
        """
        Nested class for CombineToRaster settings.
        """
        default_settings = {}
        
    _option_registry = {
        'COMBINETORASTER': _CombineToRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Conflate Feature Geometry
class ConflateFeatureGeometry(CarisBatchCommand):
    """
    The ConflateFeatureGeometry class conflates the edges and points of input features and saves them to the output.
    This process repairs area and line features with overlapping edges and redundant point spatials.

    Attributes:
        _command (str): The command associated with the 'Conflate Feature Geometry' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ConflateFeatureGeometry'
    _option_key = None

    _common_settings = {
        "extent": None,
        "feature_catalogue": None,
        "tolerance": None
    }

    class _ConflateFeatureGeometrySettings:
        """
        Nested class for ConflateFeatureGeometry settings.
        """
        default_settings = {}
        
    _option_registry = {
        'CONFLATEFEATUREGEOMETRY': _ConflateFeatureGeometrySettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contour Raster
class ContourRaster(CarisBatchCommand):
    """
    The ContourRaster class generates isolines to mark areas of constant value in a raster or variable resolution surface dataset.

    Attributes:
        _command (str): The command associated with the 'Contour Raster' process.
        _option_key (str): Key to identify specific settings for the process based on the output format.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ContourRaster'
    _option_key = 'output_format'

    _common_settings = {
        "output_format": None,
        "input_band": None,
        "range": None,
        "level": None,
        "level_file": None,
        "generation_method": None
    }

    class _HOBSettings:
        """
        Nested class for ContourRaster settings specific to HOB output format.
        """
        default_settings = {
            "feature_catalogue": None,
            "contour_feature": None,
            "level_attribute": None,
            "boundary_feature": None,
            "polygon_feature": None
        }

    class _DXFSettings:
        """
        Nested class for ContourRaster settings specific to DXF output format.
        """
        default_settings = {
            "boundary_name": None,
            "contour_name": None
        }
        
    _option_registry = {
        'HOB': _HOBSettings,
        'DXF': _DXFSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copy to CSAR
class CopyToCSAR(CarisBatchCommand):
    """
    The CopyToCSAR class is used for copying a point cloud, raster surface, or raster image in a supported format to CSAR format. 
    This operation reorders the data in the file and removes empty blocks when applicable.

    Attributes:
        _command (str): The command associated with the 'Copy to CSAR' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CopyToCSAR'
    _option_key = None

    _common_settings = {
        # No specific settings are needed as per the process description.
    }

    class _CopyToCSARSettings:
        """
        Nested class for CopyToCSAR settings. 
        """
        default_settings = {}
        
    _option_registry = {
        'COPYTOCSAR': _CopyToCSARSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create Depth Areas
class CreateDepthAreas(CarisBatchCommand):
    """
    The CreateDepthAreas class is used to create attributed area objects from existing lines, 
    optionally using a reference coverage.

    Attributes:
        _command (str): The command associated with the 'Create Depth Areas' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateDepthAreas'
    _option_key = None

    _common_settings = {
        "area_features": None,
        "elevation_lookup": None,
        "depth_areas": None,
        "resolve_isolations": None,
        "feature_catalogue": None
    }

    class _CreateDepthAreasSettings:
        """
        Nested class for CreateDepthAreas settings.
        """
        default_settings = {}
        
    _option_registry = {
        'CREATEDEPTHAREAS': _CreateDepthAreasSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create Soundings from Coverage
class CreateSoundingsFromCoverage(CarisBatchCommand):
    """
    The CreateSoundingsFromCoverage class creates sounding features from a subset of nodes in a coverage.

    Attributes:
        _command (str): The command associated with the 'Create Soundings from Coverage' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateSoundingsFromCoverage'
    _option_key = None

    _common_settings = {
        "input_band": None,
        "minimum_distance": None,
        "scale": None,
        "selection_bias": None,
        "apply_designated": None,
        "feature_catalogue": None,
        "mapping_file": None
    }

    class _CreateSoundingsFromCoverageSettings:
        """
        Nested class for CreateSoundingsFromCoverage settings.
        """
        default_settings = {}
        
    _option_registry = {
        'CREATESOUNDINGSFROMCOVERAGE': _CreateSoundingsFromCoverageSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Delete Band
class DeleteBand(CarisBatchCommand):
    """
    The DeleteBand class is used to permanently delete band information from a CSAR file.

    Attributes:
        _command (str): The command associated with the 'Delete Band' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'DeleteBand'
    _option_key = None

    _common_settings = {
        "input_band": None
    }

    class _DeleteBandSettings:
        """
        Nested class for DeleteBand settings.
        """
        default_settings = {}
        
    _option_registry = {
        'DELETEBAND': _DeleteBandSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Difference Coverages
class DifferenceCoverages(CarisBatchCommand):
    """
    The DifferenceCoverages class subtracts the difference file coverage specified in the options from the input coverage.

    Attributes:
        _command (str): The command associated with the 'Difference Coverages' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'DifferenceCoverages'
    _option_key = 'difference_type'

    _common_settings = {
        "difference_type": None,
        "input_band": None,
        "difference_file": None,
        "comments": None
    }

    class _RasterSettings:
        """
        Nested class for Raster settings.
        """
        default_settings = {
            "difference_band": None
        }

    class _ReferenceModelSettings:
        """
        Nested class for Reference Model settings.
        """
        default_settings = {
            "template_name": None
        }

    _option_registry = {
        "RASTER": _RasterSettings,
        "REFERENCEMODEL": _ReferenceModelSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Expand Isolations for Cartography
class ExpandIsolationsForCartography(CarisBatchCommand):
    """
    The ExpandIsolationsForCartography class ensures all isolations are large enough to enclose a sounding at the specified chart scale.

    Attributes:
        _command (str): The command associated with the 'Expand Isolations for Cartography' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExpandIsolationsForCartography'
    _option_key = None

    _common_settings = {
        "size": None,
        "scale": None,
        "limiting_features": None,
        "feature_catalogue": None,
        "elevation_lookup": None,
        "sounding_rounding": None,
        "sounding_rounding_file": None,
        "critical_points": None,
        "critical_points_band": None
    }

    class _ExpandIsolationsForCartographySettings:
        """
        Nested class for ExpandIsolationsForCartography settings.
        """
        default_settings = {}
        
    _option_registry = {
        'EXPANDISOLATIONSFORCARTOGRAPHY': _ExpandIsolationsForCartographySettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export Coverage Metadata
class ExportCoverageMetadata(CarisBatchCommand):
    """
    The ExportCoverageMetadata class writes metadata to an XML file with a specific profile.

    Attributes:
        _command (str): The command associated with the 'Export Coverage Metadata' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportCoverageMetadata'
    _option_key = 'profile'

    _common_settings = {
        "profile": None,
        
    }

    class _BAGSettings:
        """
        Nested class for BAG settings.
        """
        default_settings = {
            "uncertainty_type": None,
            "abstract": None,
            "status": None,
            "vertical_datum": None,
            "party_name": None,
            "party_position": None,
            "party_organization": None,
            "party_role": None,
            "legal_constraints": None,
            "other_constraints": None,
            "security_constraints": None,
            "notes": None
        }

    class _ISO19115Settings:
        """
        Nested class for ISO19115 settings.
        """
        default_settings = {}

    _option_registry = {
        "BAG": _BAGSettings,
        "ISO19115": _ISO19115Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export Coverage to ASCII
class ExportCoverageToASCII(CarisBatchCommand):
    """
    The ExportCoverageToASCII class exports band values from a coverage to an ASCII file.

    Attributes:
        _command (str): The command associated with the 'Export Coverage to ASCII' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportCoverageToASCII'
    _option_key = None

    _common_settings = {
        "include": None,
        "include_rejected": None,
        "include_header": None,
        "delimiter": None,
        "output_crs": None,
        "coordinate_format": None,
        "coordinate_precision": None,
        "include_band": None,
        "z_axis_convention": None,
        "band_filter": None,
        "sample": None,
        "elevation_unit": None,
        "coordinate_unit": None,
        "other_unit": None
    }

    class _ExportCoverageToASCIISettings:
        """
        Nested class for ExportCoverageToASCII settings.
        """
        default_settings = {}
        
    _option_registry = {
        'EXPORTCOVERAGETOASCII': _ExportCoverageToASCIISettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export Points
class ExportPoints(CarisBatchCommand):
    """
    The ExportPoints class exports band values from a coverage to a point cloud in a supported format.

    Attributes:
        _command (str): The command associated with the 'Export Points' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportPoints'
    _option_key = 'output_format'

    _common_settings = {
        "output_format": None,
    }

    class _CSARSettings:
        """
        Nested class for CSAR format settings.
        """
        default_settings = {
            "include_band": None,
            "comments": None
        }

    class _FAUSettings:
        """
        Nested class for FAU format settings.
        """
        default_settings = {}

    class _GSFSettings:
        """
        Nested class for GSF format settings.
        """
        default_settings = {
            "time_band": None,
            "beam_order_band": None,
            "include_band": None
        }

    class _LASSettings:
        """
        Nested class for LAS format settings.
        """
        default_settings = {
            "las_version": None,
            "point_record_format": None,
            "include_band": None,
            "coordinate_precision": None,
            "elevation_precision": None,
            "use_gps_week_time": None,
            "override_classification_file": None,
            "override_classification_mapping": None
        }

    _option_registry = {
        "CSAR": _CSARSettings,
        "FAU": _FAUSettings,
        "GSF": _GSFSettings,
        "LAS": _LASSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export Raster
class ExportRaster(CarisBatchCommand):
    """
    The ExportRaster class is used to export a raster dataset in one format to another format while maintaining its 
    coordinate reference system, geographic extents, and values.

    Attributes:
        _command (str): The command associated with the 'Export Raster' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportRaster'
    _option_key = 'output_format'

    _common_settings = {
        "output_format": None,
    }
    
    class _BAGSettings:
        """
        Nested class for BAG-specific settings.
        """
        default_settings = {
            "include_band": None,
            "uncertainty": None,
            "compression_level": None
        }

    class _ESRIAsciiSettings:
        """
        Nested class for ESRI ASCII-specific settings.
        """
        default_settings = {
            "include_band": None,
            "decimal_precision": None
        }

    class _USGSDemSettings:
        """
        Nested class for USGS DEM-specific settings.
        """
        default_settings = {
            "include_band": None,
            "decimal_precision": None
        }

    class _GeoTIFFSettings:
        """
        Nested class for GeoTIFF-specific settings.
        """
        default_settings = {
            "include_band": None,
            "compression": None,
            "create_tfw": False
        }

    class _PNGSettings:
        """
        Nested class for PNG-specific settings.
        """
        default_settings = {
            "include_band": None,
        }

    class _JPEGSettings:
        """
        Nested class for JPEG-specific settings.
        """
        default_settings = {
            "include_band": None,
        }

    class _S102Settings:
        """
        Nested class for S102-specific settings.
        """
        default_settings = {
            "primary_band": None,
            "uncertainty": None,
            "s100_vertical_datum": None,
            "metadata": False
        }

    class _CSARSettings:
        """
        Nested class for CSAR-specific settings.
        """
        default_settings = {
            "include_band": None,
        }

    _option_registry = {
        "BAG": _BAGSettings,
        "ESRI_ASCII": _ESRIAsciiSettings,
        "USGS_DEM": _USGSDemSettings,
        "GEOTIFF": _GeoTIFFSettings,
        "PNG": _PNGSettings,
        "JPEG": _JPEGSettings,
        "S102": _S102Settings,
        "CSAR": _CSARSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export Raster to STL
class ExportRasterToSTL(CarisBatchCommand):
    """
    The ExportRasterToSTL class exports raster band values to the STL format for 3D printing.

    Attributes:
        _command (str): The command associated with the 'Export Raster to STL' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportRasterToSTL'
    _option_key = None

    _common_settings = {
        "vertical_exaggeration": None,
        "include_band": None,
        "scale": None,
        "output_as_ascii": None
    }

    class _ExportRasterToSTLSettings:
        """
        Nested class for ExportRasterToSTL settings.
        """
        default_settings = {}
        
    _option_registry = {
        'EXPORTRASTERTOSTL': _ExportRasterToSTLSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Extract Coverage
class ExtractCoverage(CarisBatchCommand):
    """
    The ExtractCoverage class extracts a portion of a coverage.

    Attributes:
        _command (str): The command associated with the 'Extract Coverage' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExtractCoverage'
    _option_key = None

    _common_settings = {
        "include_band": None,
        "extract_type": None,
        "include_rejected": None,
        "band_filter": None,
        "geometry": None,
        "geometry_file": None,
        "comments": None
    }

    class _ExtractCoverageSettings:
        """
        Nested class for ExtractCoverage settings.
        """
        default_settings = {}
        
    _option_registry = {
        'EXTRACTCOVERAGE': _ExtractCoverageSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Fill Raster Holidays
class FillRasterHolidays(CarisBatchCommand):
    """
    The FillRasterHolidays class uses the mean of nearby nodes to fill cells in holidays in a raster dataset.

    Attributes:
        _command (str): The command associated with the 'Fill Raster Holidays' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FillRasterHolidays'
    _option_key = None

    _common_settings = {
        "input_band": None,
        "matrix": None,
        "include_band": None
    }

    class _FillRasterHolidaysSettings:
        """
        Nested class for FillRasterHolidays settings.
        """
        default_settings = {}
        
    _option_registry = {
        'FILLRASTERHOLIDAYS': _FillRasterHolidaysSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter Coverage
class FilterCoverage(CarisBatchCommand):
    """
    The FilterCoverage class creates a new coverage with nodes that meet specified criteria.

    Attributes:
        _command (str): The command associated with the 'Filter Coverage' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FilterCoverage'
    _option_key = None

    _common_settings = {
        "include_band": None,
        "expression": None
    }

    class _FilterCoverageSettings:
        """
        Nested class for FilterCoverage settings.
        """
        default_settings = {}
        
    _option_registry = {
        'FILTERCOVERAGE': _FilterCoverageSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Finalize Raster
class FinalizeRaster(CarisBatchCommand):
    """
    The FinalizeRaster class embeds designated soundings into the primary elevation band of a raster dataset.

    Attributes:
        _command (str): The command associated with the 'Finalize Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FinalizeRaster'
    _option_key = None

    _common_settings = {
        "include_band": None,
        "apply_designated": None,
        "min_uncertainty": None,
        "uncertainty_source": None,
        "filter": None,
        "comments": None
    }

    class _FinalizeRasterSettings:
        """
        Nested class for FinalizeRaster settings.
        """
        default_settings = {}
        
    _option_registry = {
        'FINALIZERASTER': _FinalizeRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Generalize Raster
class GeneralizeRaster(CarisBatchCommand):
    """
    The GeneralizeRaster class modifies elevation values of a raster surface using a 3D double buffering rolling ball algorithm.

    Attributes:
        _command (str): The command associated with the 'Generalize Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'GeneralizeRaster'
    _option_key = None

    _common_settings = {
        "include_band": None,
        "resolution": None,
        "radius": None,
        "defocus_radius": None,
        "apply_designated": None,
        "comments": None
    }

    class _GeneralizeRasterSettings:
        """
        Nested class for GeneralizeRaster settings.
        """
        default_settings = {}
        
    _option_registry = {
        'GENERALIZERASTER': _GeneralizeRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Grid Points
class GridPoints(CarisBatchCommand):
    """
    The GridPoints class creates a CSAR raster from a CSAR point cloud using a gridding method.

    Attributes:
        _command (str): The command associated with the 'Grid Points' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'GridPoints'
    _option_key = None

    _common_settings = {
        "primary_band": None,
        "resolution": None,
        "include_band": None,
        "degrees_of_freedom": None,
        "anchor": None,
        "comments": None
    }

    class _GridPointsSettings:
        """
        Nested class for GridPoints settings.
        """
        default_settings = {}
        
    _option_registry = {
        'GRIDPOINTS': _GridPointsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Grid Points Using CUBE
class GridPointsUsingCUBE(CarisBatchCommand):
    """
    The GridPointsUsingCUBE class creates a raster surface based on a CUBE algorithm from source points in CSAR format.

    Attributes:
        _command (str): The command associated with the 'Grid Points Using CUBE' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'GridPointsUsingCUBE'
    _option_key = None

    _common_settings = {
        "resolution": None,
        "extent": None,
        "anchor": None,
        "output_crs": None,
        "output_vertical_crs": None,
        "input_band": None,
        "primary_band": None,
        "vertical_uncertainty": None,
        "horizontal_uncertainty": None,
        "disambiguation_method": None,
        "cube_config_file": None,
        "cube_config_name": None,
        "cube_config_settings": None,
        "iho_order": None,
        "iho_limits": None,
        "use_chgf_distance": None,
        "comments": None
    }

    class _GridPointsUsingCUBESettings:
        """
        Nested class for GridPointsUsingCUBE settings.
        """
        default_settings = {}
        
    _option_registry = {
        'GRIDPOINTUSINGCUBE': _GridPointsUsingCUBESettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import Points
class ImportPoints(CarisBatchCommand):
    """
    The ImportPoints class creates a CSAR file from input points in a specified format.

    Attributes:
        _command (str): The command associated with the 'Import Points' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportPoints'
    _option_key = 'input_format'

    _common_settings = {
        "input_format": None,
        "gridding_method": None,
        "resolution": None,
        "extent": None,
        "output_crs": None,
        "output_vertical_crs": None,
        "compute_band": None,
        "include_band": None,
        "recurse": None,
        "primary_band": None,
        "temporal_extent": None,
        "anchor": None,
        "comments": None
    }

    class _ASCII_Settings:
        """
        Nested class for ASCII settings.
        """
        default_settings = {
            "input_crs": None,
            "info_file": None
        }

    class _CSAR_Settings:
        """
        Nested class for CSAR settings.
        """
        default_settings = {
            "input_band": None
        }

    class _C_AND_C_Settings:
        """
        Nested class for C&C settings.
        """
        default_settings = {
            "input_crs": None,
            "z_axis_convention": None
        }

    class _FAU_Settings:
        """
        Nested class for FAU settings.
        """
        default_settings = {
            "roll_angle_multiplier": None,
            "beam_setting": None,
            "filter_duplicates": None
        }

    class _GSF_Settings:
        """
        Nested class for GSF settings.
        """
        default_settings = {
            "z_axis_convention": None
        }

    class _HOB_Settings:
        """
        Nested class for HOB settings.
        """
        default_settings = {
            "feature_catalogue": None
        }

    class _HTF_Settings:
        """
        Nested class for HTF settings.
        """
        default_settings = {
            "input_crs": None,
            "depth_attribute": None,
            "depth_scale_factor": None,
            "v_uncert_attribute": None,
            "x_coord_attribute": None,
            "y_coord_attribute": None,
            "z_axis_convention": None
        }

    class _HYD93_Settings:
        """
        Nested class for HYD93 settings.
        """
        default_settings = {
            "input_crs": None,
            "z_axis_convention": None
        }

    class _LAS_Settings:
        """
        Nested class for LAS settings.
        """
        default_settings = {
            "override_crs": None,
            "override_classification_file": None,
            "override_classification_mapping": None,
            "use_las_extent": None,
            "z_axis_convention": None,
            "flag_synthetic": None,
            "flag_key_point": None,
            "flag_overlap": None,
            "flag_withheld": None,
            "reference_week": None
        }

    class _NTX_Settings:
        """
        Nested class for NTX settings.
        """
        default_settings = {
            "flag_selected": None,
            "flag_suppressed": None,
            "flag_background": None,
            "include_3D_symbol": None,
            "z_axis_convention": None
        }

    class _RDP_Settings:
        """
        Nested class for RDP settings.
        """
        default_settings = {
            "z_axis_convention": None
        }

    _option_registry = {
        "ASCII": _ASCII_Settings,
        "CSAR": _CSAR_Settings,
        "C_AND_C": _C_AND_C_Settings,
        "FAU": _FAU_Settings,
        "GSF": _GSF_Settings,
        "HOB": _HOB_Settings,
        "HTF": _HTF_Settings,
        "HYD93": _HYD93_Settings,
        "LAS": _LAS_Settings,
        "NTX": _NTX_Settings,
        "RDP": _RDP_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Join Points
class JoinPoints(CarisBatchCommand):
    """
    The JoinPoints class creates a new point cloud from the points in the inputs.

    Attributes:
        _command (str): The command associated with the 'Join Points' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'JoinPoints'
    _option_key = None

    _common_settings = {
        "primary_band": None,
        "contributor_attribute": None,
        "extent": None,
        "output_crs": None,
        "output_vertical_crs": None,
        "comments": None
    }

    class _JoinPointsSettings:
        """
        Nested class for JoinPoints settings.
        """
        default_settings = {}
        
    _option_registry = {
        'JOINPOINTS': _JoinPointsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Rebalance Points
class RebalancePoints(CarisBatchCommand):
    """
    The RebalancePoints class modifies the point cloud to ensure a more uniform visualization 
    by adjusting which points are shown at each display level.

    Attributes:
        _command (str): The command associated with the 'Rebalance Points' process.
        _option_key (str): Key to identify specific settings for the process, set to None as there are no options.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RebalancePoints'
    _option_key = None

    _common_settings = {
        # No additional settings or options for this process
    }

    class _RebalancePointsSettings:
        """
        Nested class for RebalancePoints settings.
        """
        default_settings = {}
        
    _option_registry = {
        'REBALANCEPOINTS': _RebalancePointsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Remove Deep Isolations
class RemoveDeepIsolations(CarisBatchCommand):
    """
    The RemoveDeepIsolations class deletes closed lines representing deep isolations that are smaller 
    than a specified threshold.

    Attributes:
        _command (str): The command associated with the 'Remove Deep Isolations' process.
        _option_key (str): Key to identify specific settings for the process, set to None as there are no options.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RemoveDeepIsolations'
    _option_key = None

    _common_settings = {
        "minimum_area": None,
        "scale": None,
        "feature_catalogue": None,
        "elevation_lookup": None
    }

    class _RemoveDeepIsolationsSettings:
        """
        Nested class for RemoveDeepIsolations settings.
        """
        default_settings = {}
        
    _option_registry = {
        'REMOVEDEEPISOLATIONS': _RemoveDeepIsolationsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Render Raster
class RenderRaster(CarisBatchCommand):
    """
    The RenderRaster class exports a raster band to an image by converting the values into colours.
    
    Attributes:
        _command (str): The command associated with the 'Render Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as there are no options.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RenderRaster'
    _option_key = None

    _common_settings = {
        "input_band": None,
        "colour_file": None,
        "colour_range": None,
        "reverse_colours": None,
        "enable_shading": None,
        "shading": None,
        "exaggeration": None,
        "filter": None,
        "transparency": None,
        "z_convention": None
    }

    class _RenderRasterSettings:
        """
        Nested class for RenderRaster settings.
        """
        default_settings = {}

    _option_registry = {
        'RENDERRASTER': _RenderRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Repair Coverage
class RepairCoverage(CarisBatchCommand):
    """
    The RepairCoverage class modifies a coverage to fix specified issues.
    This process is useful for addressing issues identified by the Validate Coverage process.

    Attributes:
        _command (str): The command associated with the 'Repair Coverage' process.
        _option_key (str): Key to identify specific settings for the process, set to None as there are no specific options.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RepairCoverage'
    _option_key = None

    _common_settings = {
        "reindex_cloud": None
    }

    class _RepairCoverageSettings:
        """
        Nested class for RepairCoverage settings.
        """
        default_settings = {}

    _option_registry = {
        'REPAIRCOVERAGE': _RepairCoverageSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Resample Surface To Raster
class ResampleSurfaceToRaster(CarisBatchCommand):
    """
    The ResampleSurfaceToRaster class creates a fixed resolution raster surface 
    by interpolating a fixed or variable resolution surface at a single resolution.

    Attributes:
        _command (str): The command associated with the 'Resample Surface To Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ResampleSurfaceToRaster'
    _option_key = None

    _common_settings = {
        "resolution": None,
        "extent": None,
        "type": None,
        "minimum_neighbours": None,
        "tautness": None,
        "grid_linearity": None
    }

    class _ResampleSurfaceToRasterSettings:
        """
        Nested class for ResampleSurfaceToRaster settings.
        """
        default_settings = {}

    _option_registry = {
        'RESAMPLESURFACETORASTER': _ResampleSurfaceToRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Shift Elevation Bands
class ShiftElevationBands(CarisBatchCommand):
    """
    The ShiftElevationBands class alters elevation band values by the specified method.

    Attributes:
        _command (str): The command associated with the 'Shift Elevation Bands' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ShiftElevationBands'
    _option_key = 'shift_type'

    _common_settings = {
        "input_band": None,
        "include_band": None,
        "shift_type": None,
        "output_vertical_crs": None,
        "comments": None
    }

    class _ASCII_Settings:
        """
        Nested class for ASCII shift type settings.
        """
        default_settings = {
            "shift_file": None
        }

    class _Value_Settings:
        """
        Nested class for VALUE shift type settings.
        """
        default_settings = {
            "shift_value": None
        }

    class _Tide_Settings:
        """
        Nested class for TIDE shift type settings.
        """
        default_settings = {
            "shift_file": None,
            "date_band": None,
            "time_band": None
        }

    class _Raster_Settings:
        """
        Nested class for RASTER shift type settings.
        """
        default_settings = {
            "shift_file": None,
            "elevation_band": None
        }

    class _SPINE_Settings:
        """
        Nested class for SPINE shift type settings.
        """
        default_settings = {
            "username": None,
            "password": None,
            "url": None,
            "proxy": None,
            "time": None
        }

    _option_registry = {
        "ASCII": _ASCII_Settings,
        "VALUE": _Value_Settings,
        "TIDE": _Tide_Settings,
        "RASTER": _Raster_Settings,
        "SPINE": _SPINE_Settings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Smooth Features by Direction Bias
class SmoothFeaturesByDirectionBias(CarisBatchCommand):
    """
    The SmoothFeaturesByDirectionBias class alters line and area features by applying a direction-biased 
    safe-side smoothing algorithm.

    Attributes:
        _command (str): The command associated with the 'Smooth Features By Direction Bias' process.
        _option_key (str): Key to identify specific settings for the process. It's set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'SmoothFeaturesByDirectionBias'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "tolerance": None,
        "maximum_edge": None,
        "spline_density": None,
        "convergence": None,
        "iterations": None,
        "scale": None,
        "working_crs": None,
        "direction_bias": None,
        "blocking_feature": None
    }

    class _SmoothFeaturesByDirectionBiasSettings:
        """
        Nested class for SmoothFeaturesByDirectionBias settings.
        """
        default_settings = {}
        
    _option_registry = {
        'SMOOTHFEATURESBYDIRECTIONBIAS': _SmoothFeaturesByDirectionBiasSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Split Coverage
class SplitCoverage(CarisBatchCommand):
    """
    The SplitCoverage class creates new coverages for each set of data that meets a specified criteria.

    Attributes:
        _command (str): The command associated with the 'Split Coverage' process.
        _option_key (str): Key to identify specific settings for the process, set to 'method'.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'SplitCoverage'
    _option_key = 'method'

    _common_settings = {
        "method": None,
    }

    class _ValueSettings:
        """
        Nested class for SplitCoverage settings when using the 'Value' method.
        """
        default_settings = {
            "input_band": None
        }
        
    _option_registry = {
        'VALUE': _ValueSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Thin Points
class ThinPoints(CarisBatchCommand):
    """
    The ThinPoints class creates a new point cloud with a subset of the points from the input.

    Attributes:
        _command (str): The command associated with the 'Thin Points' process.
        _option_key (str): Key to identify specific settings for the process, set to 'method'.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ThinPoints'
    _option_key = 'method'

    _common_settings = {
        "method": None,
        "include_band": None,
        "comments": None
    }

    class _RandomSettings:
        """
        Nested class for ThinPoints settings when using the 'RANDOM' method.
        """
        default_settings = {
            "percentage": None
        }

    class _MinimumDistanceSettings:
        """
        Nested class for ThinPoints settings when using the 'MINIMUM_DISTANCE' method.
        """
        default_settings = {
            "minimum_distance": None,
            "scale": None
        }
    
    class _ApplyBiasSettings:
        """
        Nested class for ThinPoints settings when using the 'APPLY_BIAS' method.
        """
        default_settings = {
            "input_band": None,
            "bias": None,
            "minimum_distance": None,
            "scale": None,
            "apply_designated": None
        }

    _option_registry = {
        'RANDOM': _RandomSettings,
        'MINIMUM_DISTANCE': _MinimumDistanceSettings,
        'APPLY_BIAS': _ApplyBiasSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Tile Raster
class TileRaster(CarisBatchCommand):
    """
    The TileRaster class exports a single raster to one or more raster files based on the defined tiling scheme.

    Attributes:
        _command (str): The command associated with the 'Tile Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'TileRaster'
    _option_key = None

    _common_settings = {
        "size": None,
        "buffer": None
    }

    class _TileRasterSettings:
        """
        Nested class for TileRaster settings.
        """
        default_settings = {}
        
    _option_registry = {
        'TILERASTER': _TileRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update Band Values
class UpdateBandValues(CarisBatchCommand):
    """
    The UpdateBandValues class changes values for all nodes that pass the criteria in an expression.

    Attributes:
        _command (str): The command associated with the 'Update Band Values' process.
        _option_key (str): Key to identify specific settings for the process, set to 'band-type'.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateBandValues'
    _option_key = 'band-type'

    _common_settings = {
        "band_type": None,
        "expression": None,
        "geometry": None,
        "geometry_file": None,
        "geometry_type": None
    }

    class _NumericBandSettings: #NUMBERIC
        """
        Nested class for Numeric Band settings.
        """
        default_settings = {
            "input_band": None,
            "value": None
        }

    class _StatusBandSettings:
        """
        Nested class for Status Band settings.
        """
        default_settings = {
            "value": None
        }
        
    _option_registry = {
        'NUMERIC': _NumericBandSettings, #NUMBERIC
        'STATUS': _StatusBandSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Validate Coverage
class ValidateCoverage(CarisBatchCommand):
    """
    The ValidateCoverage class reports whether the input coverage has any of a set of known data corruption issues.

    Attributes:
        _command (str): The command associated with the 'Validate Coverage' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ValidateCoverage'
    _option_key = None

    _common_settings = {}

    class _ValidateCoverageSettings:
        """
        Nested class for ValidateCoverage settings.
        """
        default_settings = {}
        
    _option_registry = {
        'VALIDATECOVERAGE': _ValidateCoverageSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Vectorize Raster
class VectorizeRaster(CarisBatchCommand):
    """
    The VectorizeRaster class produces polygons from raster pixels.

    Attributes:
        _command (str): The command associated with the 'Vectorize Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'VectorizeRaster'
    _option_key = None

    _common_settings = {
        "input_band": None,
        "feature_catalogue": None,
        "polygon_feature": None,
        "mode": None,
        "value_attribute": None,
        "component_attribute": None
    }

    class _VectorizeRasterSettings:
        """
        Nested class for VectorizeRaster settings.
        """
        default_settings = {}
        
    _option_registry = {
        'VECTORIZERASTER': _VectorizeRasterSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Warp Points
class WarpPoints(CarisBatchCommand):
    """
    The WarpPoints class transforms points to a specified coordinate reference system.

    Attributes:
        _command (str): The command associated with the 'Warp Points' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'WarpPoints'
    _option_key = None

    _common_settings = {
        "output_crs": None,
        "output_vertical_crs": None,
        "primary_band": None,
        "include_band": None,
        "comments": None
    }

    class _WarpPointsSettings:
        """
        Nested class for WarpPoints settings.
        """
        default_settings = {}
        
    _option_registry = {
        'WARPPOINTS': _WarpPointsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Warp Raster
class WarpRaster(CarisBatchCommand):
    """
    The WarpRaster class transforms a raster surface to a specified coordinate reference system.

    Attributes:
        _command (str): The command associated with the 'Warp Raster' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'WarpRaster'
    _option_key = None

    _common_settings = {
        "output_crs": None,
        "output_vertical_crs": None,
        "primary_band": None,
        "resolution": None,
        "reprojection_method": None,
        "input_band": None,
        "comments": None,
        "recompute_stat": None,
        "anchor": None
    }

    class _WarpRasterSettings:
        """
        Nested class for WarpRaster settings.
        """
        default_settings = {}
        
    _option_registry = {
        'WARPRASTER': _WarpRasterSettings
    }
