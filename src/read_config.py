"""
Module for working with the user's application configuration.
"""

from pathlib import Path

from yaml import safe_load as read_yaml_file


def read_config(path_to_config: Path) -> dict:
    """Read `.yaml` or `.yml` configuration file."""
    suffixes = path_to_config.suffixes
    if suffixes:
        suffix = suffixes[-1]
        match suffix:
            case ".yml" | ".yaml":
                return read_yaml_file(path_to_config.open("r"))
            case _:
                raise ValueError("Invalid file extension")
    else:
        raise ValueError("Invalid file extension")
