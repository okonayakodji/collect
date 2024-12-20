import cli
import config
from read_config import read_config

import asyncio
import logging
import pprint
from pathlib import Path


class Collect:
    def __init__(
        self,
        path_to_config: Path,
        logger: logging.Logger,
        ignored_plugins: list[str] = [],
    ):
        self.path_to_config = path_to_config
        self.logger = logger
        self.ignored_plugins = ignored_plugins
        self.config_content = {}

    def with_parsed_config(self):
        self.config_content = read_config(self.path_to_config)
        return self

    async def run(self): ...

    async def stop(self): ...

    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)


async def main():
    args = cli.parse_args()
    logging.basicConfig(
        format=config.LOGGING_FORMAT,
        level=(logging.DEBUG if args.debug else logging.INFO),
    )
    logging.debug(f"Parsed cli args:\n\n{pprint.pformat(vars(args))}\n")

    app = Collect(args.path_to_config, logging.getLogger(__name__)).with_parsed_config()
    pprint.pprint(app)


if __name__ == "__main__":
    asyncio.run(main())
