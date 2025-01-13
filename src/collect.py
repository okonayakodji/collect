"""
program logic
"""

import logging
from pathlib import Path

import config
from work_with_yaml import parse_config


class Collect:
    """TODO"""

    def __init__(self, yaml_config: Path, logger: logging.Logger | None = None):
        """TODO"""

        self.yaml_config = yaml_config
        self.config_content = None
        self.logger = logger

    def with_parsed_config(self):
        """TODO"""

        temp_content = parse_config(self.yaml_config)
        if temp_content:
            self.config_content = temp_content.get(config.START_FIELD_IN_YAML)
        return self

    def debug(self, message: str):
        """wrapper for logging.debug"""
        if self.logger:
            self.logger.debug(message)

    def run(self):
        """TODO"""
        raise NotImplementedError

    def __repr__(self):
        return str(self.__dict__)
