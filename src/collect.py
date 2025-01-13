"""
Module for separating the main class of a program.
"""

import logging
from pathlib import Path

import config
from work_with_yaml import parse_config


class Collect:
    """
    The main class of the program.
    It is needed to initialize the configuration and launch plugins.
    """

    def __init__(self, yaml_config: Path, logger: logging.Logger | None = None):
        """
        Default init.
        """

        self.yaml_config = yaml_config
        self.config_content = None
        self.logger = logger

    def with_parsed_config(self):
        """
        Factory method to update class with parsed config file.
        """

        temp_content = parse_config(self.yaml_config)
        if temp_content:
            self.config_content = temp_content.get(config.START_FIELD_IN_YAML)
        return self

    def debug(self, message: str):
        """
        Wrapper for `logging.debug`.
        """

        if self.logger:
            self.logger.debug(message)

    def run(self):
        """
        Function to start the instance.
        Will recheck plugins every few specified seconds.
        """

        raise NotImplementedError

    def __repr__(self):
        return str(self.__dict__)
