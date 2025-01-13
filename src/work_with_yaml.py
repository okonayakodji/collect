"""
Module for working with `.yaml` file.
"""

from pathlib import Path

from yaml import safe_load as parse_yaml


def parse_config(config: Path):
    """
    Checks the validity of the configuration file and parses it.
    """

    if config.suffixes:
        suffix = config.suffixes[-1]
        match suffix:
            case ".yaml" | ".yml":
                return parse_yaml(config.open("r"))
            case _:
                raise ValueError("Invalid file extension")
    else:
        raise ValueError("Invalid file extension")
