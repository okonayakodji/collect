"""
Internal app config.
"""

DEFAULT_PATH_TO_CONFIG = "./collect.yaml"
LOGGING_FORMAT = "%(asctime)s [%(levelname)s]: %(message)s"
DEFAULT_RECHECK_TIMER = 3

# Field in the yaml configuration file that will be used
# to configure plugins. Other fields will be ignored.
# This is necessary for convenient use of .yaml anchors.
START_FIELD_IN_YAML = "plugins"
