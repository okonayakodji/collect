"""
Module for separating the main class of a program.
"""

import logging
from pathlib import Path
from sys import exit as sys_exit
from time import sleep

import config
from work_with_yaml import parse_config
from plugins.plugin import REGISTRY


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

    def debug(self, message: str):
        """
        Wrapper for `logging.debug`.
        """

        if self.logger:
            self.logger.debug(message)

    def info(self, message: str):
        """
        Wrapper for `logging.info`.
        """

        if self.logger:
            self.logger.info(message)

    def error(self, message: str):
        """
        Wrapper for `logging.error`.
        """

        if self.logger:
            self.logger.error(message)

    def with_parsed_config(self):
        """
        Factory method to update class with parsed config file.
        """

        temp_content = parse_config(self.yaml_config)
        self.debug(f"Parsed content from the config file:\n{temp_content}")
        if temp_content:
            self.config_content = temp_content.get(config.START_FIELD_IN_YAML)
        return self

    def run(self, recheck_timer: int):
        """
        Function to start the instance.
        Will recheck plugins every few specified seconds.
        """

        try:
            while True:
                plugins = []
                for plugin, plugin_settings in self.config_content.items():
                    maybe_needed_plugin = REGISTRY.get(plugin)
                    if maybe_needed_plugin:
                        if plugin_settings:
                            plugins.append(maybe_needed_plugin(**plugin_settings))
                        else:
                            plugins.append(maybe_needed_plugin())
                self.debug(f"Generated plugins\n{plugins}")

                for plugin in plugins:
                    if plugin.is_ready():
                        plugin.run()

                sleep(recheck_timer)

        except KeyboardInterrupt:
            sys_exit()

    def __repr__(self):
        return str(self.__dict__)
