
"""
HIPS Processes Module

This module extends the CarisBatchCommand class to provide specialized functionalities 
for Hydrographic Information Processing System (HIPS) operations. It encompasses 
a diverse array of classes, each tailored to handle specific tasks within 
hydrographic data processing workflows, such as adding Kraken TIL to mosaics, 
managing HIPS grids, and updating SIPS contact positions.

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
# Add Bridges Between Matching Lines
class AddBridgesBetweenMatchingLines(CarisBatchCommand):
    """
    The AddBridgesBetweenMatchingLines class adds two lines connecting the nearest points of each pair 
    of nearby line features that have the same elevation.

    Attributes:
        _command (str): The command associated with the 'Add Bridges Between Matching Lines' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddBridgesBetweenMatchingLines'
    _option_key = None

    _common_settings = {
        "maximum_length": None,
        "distance_coefficients": None,
        "scale": None,
        "working_crs": None,
        "limiting_features": None,
        "direction_bias": None,
        "elevation_lookup": None,
        "feature_catalogue": None
    }

    class _AddBridgesBetweenMatchingLinesSettings:
        """
        Nested class for AddBridgesBetweenMatchingLines settings.
        """
        default_settings = {}
        
    _option_registry = {
        'ADDBRIDGESBETWEENMATCHINGLINES': _AddBridgesBetweenMatchingLinesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add Features
class AddFeatures(CarisBatchCommand):
    """
    The AddFeatures class copies features from the input to the output, 
    optionally maintaining feature object identifiers (FOIDs).

    Attributes:
        _command (str): The command associated with the 'Add Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddFeatures'
    _option_key = None

    _common_settings = {
        "keep_foid": None,
        "require_all": None,
        "feature_catalogue": None,
        "map_undefined_attribute_value": None,
        "map_known_attribute_value": None,
        "verified": None,
        "input_crs": None,
        "overwrite": None
    }

    class _AddFeaturesSettings:
        """
        Nested class for AddFeatures settings.
        """
        default_settings = {}
        
    _option_registry = {
        'ADDFEATURES': _AddFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Add Geometry Attributes
class AddGeometryAttributes(CarisBatchCommand):
    """
    The AddGeometryAttributes class adds geometry-related attributes to existing vector features.

    Attributes:
        _command (str): The command associated with the 'Add Geometry Attributes' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AddGeometryAttributes'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "area": None,
        "perimeter": None,
        "centroid": None,
        "length": None,
        "begin": None,
        "end": None,
        "middle": None,
        "cover": None,
        "point_count": None,
        "point": None
    }

    class _AddGeometryAttributesSettings:
        """
        Nested class for AddGeometryAttributes settings.
        """
        default_settings = {}
        
    _option_registry = {
        'ADDGEOMETRYATTRIBUTES': _AddGeometryAttributesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Buffer Features
class BufferFeatures(CarisBatchCommand):
    """
    The BufferFeatures class creates area features around existing vector features.

    Attributes:
        _command (str): The command associated with the 'Buffer Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'BufferFeatures'
    _option_key = None

    _common_settings = {
        "buffer_crs": None,
        "distance": None,
        "scale": None,
        "feature_catalogue": None,
        "area_method": None,
        "line_end_style": None
    }

    class _BufferFeaturesSettings:
        """
        Nested class for BufferFeatures settings.
        """
        default_settings = {}
        
    _option_registry = {
        'BUFFERFEATURES': _BufferFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Change Feature Attributes
class ChangeFeatureAttributes(CarisBatchCommand):
    """
    The ChangeFeatureAttributes class modifies the attributes of existing vector features.

    Attributes:
        _command (str): The command associated with the 'Change Feature Attributes' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ChangeFeatureAttributes'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "attribute": []
    }

    class _ChangeFeatureAttributesSettings:
        """
        Nested class for ChangeFeatureAttributes settings.
        """
        default_settings = {}
        
    _option_registry = {
        'CHANGEFEATUREATTRIBUTES': _ChangeFeatureAttributesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Clip Features
class ClipFeatures(CarisBatchCommand):
    """
    The ClipFeatures class trims features based on the boundaries of specified polygons.

    Attributes:
        _command (str): The command associated with the 'Clip Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ClipFeatures'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "clipper": None,
        "mark_closing_edges": False
    }

    class _ClipFeaturesSettings:
        """
        Nested class for ClipFeatures settings.
        """
        default_settings = {}
        
    _option_registry = {
        'CLIPFEATURES': _ClipFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create Areas From Lines
class CreateAreasFromLines(CarisBatchCommand):
    """
    The CreateAreasFromLines class generates area geometries from closed lines or sequences of lines forming closed shapes.

    Attributes:
        _command (str): The command associated with the 'Create Areas From Lines' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateAreasFromLines'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None
    }

    class _CreateAreasFromLinesSettings:
        """
        Nested class for CreateAreasFromLines settings.
        """
        default_settings = {}

    _option_registry = {
        'CREATEAREASFROMLINES': _CreateAreasFromLinesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create Feature Relationships
class CreateFeatureRelationships(CarisBatchCommand):
    """
    The CreateFeatureRelationships class generates master-slave relationships for input features in S-57 format.

    Attributes:
        _command (str): The command associated with the 'Create Feature Relationships' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateFeatureRelationships'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None
    }

    class _CreateFeatureRelationshipsSettings:
        """
        Nested class for CreateFeatureRelationships settings.
        """
        default_settings = {}

    _option_registry = {
        'CREATEFEATURERELATIONSHIPS': _CreateFeatureRelationshipsSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create Features From Features
class CreateFeaturesFromFeatures(CarisBatchCommand):
    """
    The CreateFeaturesFromFeatures class generates new features from each input feature, based on a specified feature code.

    Attributes:
        _command (str): The command associated with the 'Create Features From Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateFeaturesFromFeatures'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "feature_code": None
    }

    class _CreateFeaturesFromFeaturesSettings:
        """
        Nested class for CreateFeaturesFromFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'CREATEFEATURESFROMFEATURES': _CreateFeaturesFromFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create Lines From Areas
class CreateLinesFromAreas(CarisBatchCommand):
    """
    The CreateLinesFromAreas class generates closed line geometries from area features.

    Attributes:
        _command (str): The command associated with the 'Create Lines From Areas' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'CreateLinesFromAreas'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None
    }

    class _CreateLinesFromAreasSettings:
        """
        Nested class for CreateLinesFromAreas settings.
        """
        default_settings = {}

    _option_registry = {
        'CREATELINESFROMAREAS': _CreateLinesFromAreasSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Delete Features
class DeleteFeatures(CarisBatchCommand):
    """
    The DeleteFeatures class deletes features in the output that have the same primary key as features in the input.

    Attributes:
        _command (str): The command associated with the 'Delete Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'DeleteFeatures'
    _option_key = None

    _common_settings = {
        "match_by": None,
        "proposed_deletion": None,
        "input_crs": None
    }

    class _DeleteFeaturesSettings:
        """
        Nested class for DeleteFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'DELETEFEATURES': _DeleteFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Densify Features
class DensifyFeatures(CarisBatchCommand):
    """
    The DensifyFeatures class adds points to any existing segment of any edge that is longer than a threshold, 
    subdividing long segments into multiple new segments.

    Attributes:
        _command (str): The command associated with the 'Densify Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'DensifyFeatures'
    _option_key = None

    _common_settings = {
        "maximum_segment": None,
        "scale": None,
        "working_crs": None,
        "point_distribution": None,
        "feature_catalogue": None
    }

    class _DensifyFeaturesSettings:
        """
        Nested class for DensifyFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'DENSIFYFEATURES': _DensifyFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Dissolve Features
class DissolveFeatures(CarisBatchCommand):
    """
    The DissolveFeatures class removes common boundaries between areas and common nodes between lines, merging 
    adjacent or matching features in the process.

    Attributes:
        _command (str): The command associated with the 'Dissolve Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'DissolveFeatures'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "filter_file": None,
        "dissolve_into_feature_code": None,
        "primitive_type": None
    }

    class _DissolveFeaturesSettings:
        """
        Nested class for DissolveFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'DISSOLVEFEATURES': _DissolveFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Erase Features
class EraseFeatures(CarisBatchCommand):
    """
    The EraseFeatures class removes portions of input features that are inside the boundaries of a specified eraser.

    Attributes:
        _command (str): The command associated with the 'Erase Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'EraseFeatures'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "eraser": None,
        "deleted_features_filter_file": None,
        "mark_closing_edges": None
    }

    class _EraseFeaturesSettings:
        """
        Nested class for EraseFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'ERASEFEATURES': _EraseFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export Features to Shapefile
class ExportFeaturesToShapefile(CarisBatchCommand):
    """
    The ExportFeaturesToShapefile class exports features to files in Shapefile format.

    Attributes:
        _command (str): The command associated with the 'Export Features to Shapefile' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportFeaturesToShapefile'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "file_prefix": None
    }

    class _ExportFeaturesToShapefileSettings:
        """
        Nested class for ExportFeaturesToShapefile settings.
        """
        default_settings = {}

    _option_registry = {
        'EXPORTFEATURESTOSHAPEFILE': _ExportFeaturesToShapefileSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export to WKT
class ExportToWKT(CarisBatchCommand):
    """
    The ExportToWKT class exports the geometries of features to a file in Well-Known Text (WKT) format.

    Attributes:
        _command (str): The command associated with the 'Export to WKT' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportToWKT'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "elevation_lookup_file": None
    }

    class _ExportToWKTSettings:
        """
        Nested class for ExportToWKT settings.
        """
        default_settings = {}

    _option_registry = {
        'EXPORTTOWKT': _ExportToWKTSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter Features
class FilterFeatures(CarisBatchCommand):
    """
    The FilterFeatures class copies features that pass the criteria in a rule file from the input to the output.

    Attributes:
        _command (str): The command associated with the 'Filter Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FilterFeatures'
    _option_key = None

    _common_settings = {
        "extent": None,
        "feature_catalogue": None,
        "filter_file": None,
        "rule_file": None
    }

    class _FilterFeaturesSettings:
        """
        Nested class for FilterFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'FILTERFEATURES': _FilterFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Filter Features by Spatial Relation
class FilterFeaturesBySpatialRelation(CarisBatchCommand):
    """
    The FilterFeaturesBySpatialRelation class finds features that pass the criteria in a DE9IM matrix.

    Attributes:
        _command (str): The command associated with the 'Filter Features By Spatial Relation' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'FilterFeaturesBySpatialRelation'
    _option_key = None

    _common_settings = {
        "reference_geometries": None,
        "predicate": None,
        "matrix": None,
        "feature_catalogue": None
    }

    class _FilterFeaturesBySpatialRelationSettings:
        """
        Nested class for FilterFeaturesBySpatialRelation settings.
        """
        default_settings = {}

    _option_registry = {
        'FILTERFEATURESBYSPATIALRELATION': _FilterFeaturesBySpatialRelationSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Simplify Features
class SimplifyFeatures(CarisBatchCommand):
    """
    The SimplifyFeatures class removes vertices to create simpler features using the Douglas-Peucker algorithm.

    Attributes:
        _command (str): The command associated with the 'Simplify Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'SimplifyFeatures'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "tolerance": None,
        "scale": None
    }

    class _SimplifyFeaturesSettings:
        """
        Nested class for SimplifyFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'SIMPLIFYFEATURES': _SimplifyFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Smooth Features
class SmoothFeatures(CarisBatchCommand):
    """
    The SmoothFeatures class adds vertices to features using a B-spline function to smooth the features.

    Attributes:
        _command (str): The command associated with the 'Smooth Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'SmoothFeatures'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "b_spline_order": None
    }

    class _SmoothFeaturesSettings:
        """
        Nested class for SmoothFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'SMOOTHFEATURES': _SmoothFeaturesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Update Features
class UpdateFeatures(CarisBatchCommand):
    """
    The UpdateFeatures class updates features in the output using features from the input that have the same primary key.

    Attributes:
        _command (str): The command associated with the 'Update Features' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'UpdateFeatures'
    _option_key = None

    _common_settings = {
        "match_by": None,
        "require_all": None,
        "feature_catalogue": None,
        "update_relations": None,
        "certification_status": None,
        "input_crs": None,
        "map_undefined_attribute_value": None,
        "map_unknown_attribute_value": None,
        "tolerance": None,
        "match_geometry_by": None
    }

    class _UpdateFeaturesSettings:
        """
        Nested class for UpdateFeatures settings.
        """
        default_settings = {}

    _option_registry = {
        'UPDATEFEATURES': _UpdateFeaturesSettings
    }
