"""
Engineering Analysis Processes Module

This module, building upon the CarisBatchCommand class, introduces specialized 
functionalities for conducting engineering analysis within geospatial datasets. 
It encompasses classes that are crucial for volumetric calculations, contour 
generation, and other analytical processes critical in engineering and construction 
planning.

Key classes such as CalculateCoverageVolumes and ContourRasterByModel offer advanced 
tools for evaluating terrain models, computing volumes, and generating isolines. 
These functionalities are essential for assessing environmental impacts, planning 
construction projects, and other engineering-related tasks.

The classes within this module are tailored to provide precision and efficiency 
in handling complex calculations and transformations required in engineering 
analysis. They serve as vital components in the broader geospatial data processing 
and analysis workflow.

Author: Vinicius Nogueira
Created: 15-July-2020
Last Modified: 23-November-2023

Note:
    This module is an integral part of the MK-CarisAPI.
"""

from ._carisbatch import CarisBatchCommand

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Calculate Coverage Volumes
class CalculateCoverageVolumes(CarisBatchCommand):
    """
    The CalculateCoverageVolumes class is used to compare elevation data in a coverage with a model 
    to determine the volume of the difference between them.

    Attributes:
        _command (str): The command associated with the 'Calculate Coverage Volumes' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CalculateCoverageVolumes'
    _option_key = "model_type"

    _common_settings = {
        "calculation_type": None,
        "model_type": None,
        "input_band": None,
        "allowance_algorithm": None
    }

    class _FileSettings:
        """
        Nested class for File-specific settings.
        """
        default_settings = {
            "model_file": None,
            "template_name": None,
            "surface_name": None
        }

    class _PlaneSettings:
        """
        Nested class for Plane-specific settings.
        """
        default_settings = {
            "elevation": None,
            "allowance_value": 0.0
        }

    _option_registry = {
        'FILE': _FileSettings,
        'PLANE': _PlaneSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contour Raster by Model
class ContourRasterByModel(CarisBatchCommand):
    """
    The ContourRasterByModel class is used to generate isolines to mark areas of constant value from 
    a raster or variable resolution surface dataset.

    Attributes:
        _command (str): The command associated with the 'Contour Raster by Model' process.
        _option_key (str): Key to identify specific settings for the process.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ContourRasterByModel'
    _option_key = 'output_format'

    _common_settings = {
        "output_format": None,
        "input_band": None,
        "range": None,
        "level": None,
        "generation_method": None,
        "template": None,
        "add_model_elevations": None,
        "add_allowances_above": None,
        "add_allowances_below": None
    }

    class _HOBSettings:
        """
        Nested class for HOB-specific settings. 
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
        Nested class for DXF-specific settings.
        """
        default_settings = {
            "boundary_name": None,
            "contour_name": None
        }

    _option_registry = {
        'HOB': _HOBSettings,
        'DXF': _DXFSettings
    }
