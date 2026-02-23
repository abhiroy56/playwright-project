"""
Config Parser for YAML files.
"""

import yaml

from utlilities.path import CONFIGFILE_PATH


class ConfigParser:
    """
    A class to parse YAML configuration files.
    """

    @staticmethod
    def load_config(yaml_file, env) -> dict:
        """Loads the configuration for a specific environment from a YAML file."""
        with open(CONFIGFILE_PATH.joinpath(yaml_file),encoding="utf-8",) as file:
            config = yaml.safe_load(file)
        env_config = config.get(env)
        if not isinstance(env_config, dict):
            raise TypeError(f"Config for environment '{env}' is not a dictionary.")
        return env_config
