
from ._carisbatch import CarisBatchCommand

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Assign Sounding SCAMIN Values
class AssignSoundingSCAMINValues(CarisBatchCommand):
    """
    The AssignSoundingSCAMINValues class calculates minimum display scale (SCAMIN) values for S‑57 sounding 
    features using specified parameters.

    Attributes:
        _command (str): The command associated with the 'Assign Sounding SCAMIN Values' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AssignSoundingSCAMINValues'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "map_scale": None,
        "scaling_parameters_file": None
    }

    class _AssignSoundingSCAMINValuesSettings:
        """
        Nested class for AssignSoundingSCAMINValues settings.
        """
        default_settings = {}

    _option_registry = {
        'ASSIGNSOUNDINGSCAMINVALUES': _AssignSoundingSCAMINValuesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Assign Feature Scamin Values
class AssignFeatureScaminValues(CarisBatchCommand):
    """
    The AssignFeatureScaminValues class calculates minimum display scale attribute values for 
    S-57 or S-101 non-sounding features using specified parameters.

    Attributes:
        _command (str): The command associated with the 'Assign Feature Scamin Values' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'AssignFeatureScaminValues'
    _option_key = None

    _common_settings = {
        "feature_catalogue": None,
        "map_scale": None,
        "mapping_rule_file": None
    }

    class _AssignFeatureScaminValuesSettings:
        """
        Nested class for AssignFeatureScaminValues settings.
        """
        default_settings = {}

    _option_registry = {
        'ASSIGNFEATURESCAMINVALUES': _AssignFeatureScaminValuesSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Export S‑57 Product
class ExportS57Product(CarisBatchCommand):
    """
    The ExportS57Product class exports an S‑57 product as produced by the Compose module.

    Attributes:
        _command (str): The command associated with the 'Export S‑57 Product' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ExportS57Product'
    _option_key = None

    _common_settings = {
        "create_new_edition": None,
        "comment_for_dsid": None,
        "issue_date": None
    }

    class _ExportS57ProductSettings:
        """
        Nested class for ExportS57Product settings.
        """
        default_settings = {}

    _option_registry = {
        'EXPORTS57PRODUCT': _ExportS57ProductSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Modify S-57 Header
class ModifyS57Header(CarisBatchCommand):
    """
    The ModifyS57Header class modifies the header information of an S-57 file, 
    including fields in the DSID and DSPM sections.

    Attributes:
        _command (str): The command associated with the 'Modify S-57 Header' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ModifyS57Header'
    _option_key = None

    _common_settings = {
        "intended_usage": None,
        "dataset_name": None,
        "edition_number": None,
        "update_number": None,
        "issue_date": None,
        "product_specification": None,
        "iho_agency_code": None,
        "iho_agency_code_file": None,
        "dsid_comment": None,
        "compilation_scale": None,
        "dspm_comment": None
    }

    class _ModifyS57HeaderSettings:
        """
        Nested class for ModifyS57Header settings.
        """
        default_settings = {}

    _option_registry = {
        'MODIFYS57HEADER': _ModifyS57HeaderSettings
    }


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Reassign S57 FOIDs
class ReassignS57FOIDs(CarisBatchCommand):
    """
    The ReassignS57FOIDs class reassigns the feature object IDs (FOIDs) of all features in an S-57 file.
    It is used for both base and update S-57 files to ensure consistency in FOIDs across files.

    Attributes:
        _command (str): The command associated with the 'Reassign S57 FOIDs' process.
        _option_key (str): Key to identify specific settings for the process, set to None as it's not required.
        _common_settings (dict): Dictionary containing the common settings for the process.
    """

    _command = 'ReassignS57FOIDs'
    _option_key = None

    _common_settings = {
        "iho_agency_code": None,
        "iho_agency_code_file": None,
        "unique_foid_file": None,
        "foid_lookup_table_file": None
    }

    class _ReassignS57FOIDsSettings:
        """
        Nested class for ReassignS57FOIDs settings.
        """
        default_settings = {}

    _option_registry = {
        'REASSIGNS57FOIDS': _ReassignS57FOIDsSettings
    }
