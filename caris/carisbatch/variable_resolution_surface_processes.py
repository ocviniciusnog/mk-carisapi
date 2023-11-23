"""
Variable Resolution Surface Processes Module

This module extends the CarisBatchCommand class to facilitate specific Caris batch
processing tasks related to variable resolution surface processes. It encompasses
a suite of classes, each designed for a specialized task such as managing variable
resolution surfaces, adjusting surface properties, and performing advanced surface
manipulations. These classes inherit from CarisBatchCommand, leveraging its
foundational functionalities while introducing specific features and parameters
pertinent to variable resolution surface processes.

Each class within this module is meticulously crafted to encapsulate and execute
distinct Caris batch commands. This design principle ensures efficient handling
and streamlined operation of complex surface processing tasks within the Caris
environment.

Author: Vinicius Nogueira
Created: 15-July-2020
Last Modified: 23-November-2023

Note:
    This module is an integral part of the MK-CarisAPI.
"""

from ._carisbatch import CarisBatchCommand

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add to VR Surface
class AddToVRSurface(CarisBatchCommand):
    """
    The AddToVRSurface class adds source points to an existing variable resolution surface using the create 
    process parameters stored in the CSAR metadata. This process allows for updating either resolution estimates, 
    surface nodes, or both.

    Attributes:
        _command (str): The command associated with the 'Add To VR Surface' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddToVRSurface'
    _option_key = None

    _common_settings = {
        "update_type": None
    }

    class _AddToVRSurfaceSettings:
        """
        Nested class for AddToVRSurface settings.
        """
        default_settings = {}

    _option_registry = {
        'ADDTOVRSURFACE': _AddToVRSurfaceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create VR Surface
class CreateVRSurface(CarisBatchCommand):
    """
    The CreateVRSurface class creates an empty variable resolution CSAR file, setting extents and resolutions 
    based on provided source data. It includes specific settings for different estimation methods.

    Attributes:
        _command (str): The command associated with the 'Create VR Surface' process.
        _option_key (str): Key to identify specific settings for the process, set to 'estimation_method'.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateVRSurface'
    _option_key = 'estimation_method'

    _common_settings = {
        "estimation_method": None,
        "extent": None,
        "keep_partial_bins": None,
        "max_grid_size": None,
        "min_grid_size": None,
        "output_crs": None,
        "output_vertical_crs": None,
        "include_flag": None
    }

    class _CALDER_RICESettings:
        default_settings = {
            "area": None,
            "finest_resolution": None,
            "coarsest_resolution": None,
            "supergrid_size": None,
            "points_per_cell": None,
            "beam_width": None
        }

    class _CARIS_DENSITYSettings:
        default_settings = {
            "finest_resolution": None,
            "coarsest_resolution": None,
            "points_per_cell": None
        }

    class _RANGESettings:
        default_settings = {
            "input_band": None,
            "range_file": None,
            "range_table": None,
            "range_method": None,
            "range_percentile": None
        }

    _option_registry = {
        'CALDER_RICE': _CALDER_RICESettings,
        'CARIS_DENSITY': _CARIS_DENSITYSettings,
        'RANGE': _RANGESettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export VR Surface to BAG
class ExportVRSurfaceToBAG(CarisBatchCommand):
    """
    The ExportVRSurfaceToBAG class exports a variable resolution surface to a BAG raster with variable resolution 
    refinement grids. This process includes various settings related to the output BAG raster including the inclusion 
    of specific bands, uncertainty measures, legal and security constraints, and other metadata.

    Attributes:
        _command (str): The command associated with the 'Export VR Surface to BAG' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportVRSurfaceToBAG'
    _option_key = None

    _common_settings = {
        "include_band": None,
        "uncertainty": None,
        "compression_level": None,
        "representative": None,
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

    class _ExportVRSurfaceToBAGSettings:
        """
        Nested class for ExportVRSurfaceToBAG settings.
        """
        default_settings = {}

    _option_registry = {
        'EXPORTVRSURFACETOBAG': _ExportVRSurfaceToBAGSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Finalize VR Surface
class FinalizeVRSurface(CarisBatchCommand):
    """
    The FinalizeVRSurface class appends designated soundings to the primary elevation band of a variable resolution 
    surface. This process includes various settings related to the inclusion of bands, the application of designated 
    soundings, uncertainty measures, and other filtering and metadata options.

    Attributes:
        _command (str): The command associated with the 'Finalize VR Surface' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FinalizeVRSurface'
    _option_key = None

    _common_settings = {
        "include_band": None,
        "apply_designated": None,
        "include_designated_bands": None,
        "min_uncertainty": None,
        "uncertainty_source": None,
        "filter": None,
        "comments": None
    }

    class _FinalizeVRSurfaceSettings:
        """
        Nested class for FinalizeVRSurface settings.
        """
        default_settings = {}

    _option_registry = {
        'FINALIZEVRSURFACE': _FinalizeVRSurfaceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import VR Surface
class ImportVRSurface(CarisBatchCommand):
    """
    The ImportVRSurface class creates a CSAR file from an input variable resolution surface in a specified format. 
    This process supports importing data in the BAG format, specifically BAG rasters with variable resolution refinement grids.

    Attributes:
        _command (str): The command associated with the 'Import VR Surface' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ImportVRSurface'
    _option_key = None

    _common_settings = {
        "input_format": None,
        "comments": None
    }

    class _ImportVRSurfaceSettings:
        """
        Nested class for ImportVRSurface settings.
        """
        default_settings = {}

    _option_registry = {
        'IMPORTVRSURFACE': _ImportVRSurfaceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Populate VR Surface
class PopulateVRSurface(CarisBatchCommand):
    """
    The PopulateVRSurface class populates an empty variable resolution CSAR file with values for a variable resolution surface. It offers several node creation methods based on the provided input data.

    Attributes:
        _command (str): The command associated with the 'Populate VR Surface' process.
        _option_key (str): Key to identify specific settings for the process, corresponding to the population method.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'PopulateVRSurface'
    _option_key = 'population_method'

    _common_settings = {
        "population_method": None,
        "input_band": None,
        "include_flag": None,
        "primary_band": None,
        "keep_up_to_date": None,
        "comments": None
    }

    class _MEANSettings:
        """
        Nested class for MEAN population method settings.
        """
        default_settings = {
            "neighbourhood_shape": None,
            "neighbourhood_fixed": None,
            "neighbourhood_bins": None,
            "minimum_samples": None
        }

    class _IDWSettings:
        """
        Nested class for IDW population method settings.
        """
        default_settings = {
            "neighbourhood_shape": None,
            "neighbourhood_fixed": None,
            "neighbourhood_bins": None,
            "idw_power": None,
            "minimum_samples": None
        }

    class _UNCERTAINTYSettings:
        """
        Nested class for UNCERTAINTY population method settings.
        """
        default_settings = {
            "vertical_uncertainty": None,
            "horizontal_uncertainty": None,
            "iho_order": None,
            "iho_limits": None,
            "minimum_samples": None
        }

    class _CUBESettings:
        """
        Nested class for CUBE population method settings.
        """
        default_settings = {
            "vertical_uncertainty": None,
            "horizontal_uncertainty": None,
            "iho_order": None,
            "iho_limits": None,
            "disambiguation_method": None,
            "cube_config_file": None,
            "cube_config_name": None,
            "cube_config_settings": None,
            "use_chgf_distance": None
        }

    class _SELECTSettings:
        """
        Nested class for SELECT population method settings.
        """
        default_settings = {
            "bin_selection": None,
            "node_position": None,
            "include_band": None,
            "minimum_samples": None
        }

    class _SWATH_ANGLESettings:
        """
        Nested class for SWATH_ANGLE population method settings.
        """
        default_settings = {
            "angle_band": None,
            "footprint_band": None,
            "beam_width": None,
            "max_footprint": None,
            "grazing_angle_file": None,
            "grazing_angle_table": None,
            "minimum_samples": None
        }

    _option_registry = {
        'MEAN': _MEANSettings,
        'IDW': _IDWSettings,
        'UNCERTAINTY': _UNCERTAINTYSettings,
        'CUBE': _CUBESettings,
        'SELECT': _SELECTSettings,
        'SWATH_ANGLE': _SWATH_ANGLESettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Remove From VR Surface
class RemoveFromVRSurface(CarisBatchCommand):
    """
    The RemoveFromVRSurface class is used to remove source points from an existing variable resolution surface. 
    It can update resolution estimates, surface nodes, or both based on the process parameters stored in the CSAR metadata.

    Attributes:
        _command (str): The command associated with the 'Remove From VR Surface' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'RemoveFromVRSurface'
    _option_key = None

    _common_settings = {
        "update_type": None
    }

    class _RemoveFromVRSurfaceSettings:
        """
        Nested class for RemoveFromVRSurface settings.
        """
        default_settings = {}

    _option_registry = {
        'REMOVEFROMVRSURFACE': _RemoveFromVRSurfaceSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update VR CUBE Disambiguation
class UpdateVRCUBEDisambiguation(CarisBatchCommand):
    """
    The UpdateVRCUBEDisambiguation class is used to update or rerun the disambiguation method used in variable 
    resolution CUBE surfaces. This process allows choosing among different disambiguation methods.

    Attributes:
        _command (str): The command associated with the 'Update VR CUBE Disambiguation' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateVRCUBEDisambiguation'
    _option_key = None

    _common_settings = {
        "disambiguation_method": None
    }

    class _UpdateVRCUBEDisambiguationSettings:
        """
        Nested class for UpdateVRCUBEDisambiguation settings.
        """
        default_settings = {}

    _option_registry = {
        'UPDATEVRCUBEDISAMBIGUATION': _UpdateVRCUBEDisambiguationSettings
    }
