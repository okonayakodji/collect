import config

import argparse
from pathlib import Path
from sys import argv


def parse_args(args=argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path_to_config",
        type=Path,
        nargs="?",
        default=Path(config.DEFAULT_PATH_TO_CONFIG),
        help=f"path to config. Default: `{config.DEFAULT_PATH_TO_CONFIG}`",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help=f"enable debug mode",
    )
    return parser.parse_args(args)
