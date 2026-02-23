"""
Config Parser for YAML files.
"""

import yaml

from utlilities.path import CONFIGFILE_PATH


class ConfigParser:
    """
    A class to parse YAML configuration files.
    """

    def __new__(cls, yaml_file, env):
        with open(CONFIGFILE_PATH.joinpath(yaml_file),encoding="utf-8",) as file:
            config = yaml.safe_load(file)
        return config[env]
