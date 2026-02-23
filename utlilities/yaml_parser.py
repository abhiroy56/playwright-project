import yaml

from utlilities.path import CONFIGFILE_PATH


class ConfigParser:
    def __new__(cls, yaml_file, env):
        with open(CONFIGFILE_PATH.joinpath(yaml_file), 'r') as file:
            config = yaml.safe_load(file)
        return config[env]
