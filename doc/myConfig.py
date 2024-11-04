import os
import pathlib
from pathlib import Path

import yaml

_config: dict | None = None


def get_config(level1_key: str, level2_key: str | None = None) -> str:

    global _config
    if _config is None:
        load_config()

    try:
        if level2_key is None:
            return _config[level1_key]
        else:
            return _config[level1_key][level2_key]
    except KeyError:
        raise KeyError(f"Configuration for ['{level1_key}']['{level2_key}'] not found!")


def load_config(yaml_file_name: str = None):

    print(f'load configuration from {yaml_file_name}')
    if yaml_file_name is None:
        yaml_file_name = os.environ.get('TARGET_CONFIG_FILE', 'conf_prod.yaml')
    with open(pathlib.PurePath(get_project_root_path(), "configuration/" + yaml_file_name)) as yaml_file:
        config_dict = yaml.safe_load(yaml_file)

    global _config
    _config = config_dict


def get_project_root_path() -> pathlib.Path:
    return Path(__file__).parent.parent