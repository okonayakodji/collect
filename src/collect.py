"""
Program for automatic collection of daily bonuses with configuration via `.yaml` file.
"""

import asyncio
import logging
import pprint
from pathlib import Path

import cli
import config
from read_config import read_config


class Collect:
    """Main app class"""

    def __init__(
        self,
        path_to_config: Path,
        logger: logging.Logger,
        ignored_plugins: list[str] | None = None,
    ):
        """"""
        if not ignored_plugins:
            self.ignored_plugins = []
        else:
            self.ignored_plugins = ignored_plugins

        self.path_to_config = path_to_config
        self.logger = logger
        self.config_content = {}

    def with_parsed_config(self):
        """
        Factory method for modifying a class by reading a configuration file.
        """

        self.config_content = read_config(self.path_to_config)
        return self

    async def run(self):
        """Run created instance of class"""

        raise NotImplementedError

    async def stop(self):
        """Stop running instance of class"""

        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)


async def main():
    """Entry point"""

    args = cli.parse_args()

    logging.basicConfig(
        format=config.LOGGING_FORMAT,
        level=(logging.DEBUG if args.debug else logging.INFO),
    )
    logging.debug(_ := f"Parsed cli args:\n\n{pprint.pformat(vars(args))}\n")

    app = Collect(args.path_to_config, logging.getLogger(__name__)).with_parsed_config()
    pprint.pprint(app)


if __name__ == "__main__":
    asyncio.run(main())
