"""
Module for parsing command line arguments.
Moved to a separate file for ease of navigation.
"""

import argparse
from pathlib import Path
from sys import argv

import config


def parse_args(args: tuple[str] = tuple(argv[1:])):
    """
    Function for parsing command line arguments using the standard library `argparse`.

    :param `args` := Tuple of strings of required arguments.
                     Default: `sys.argv` without program file name converted to tuple.
    """

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
        help="enable debug mode",
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    print(parse_args())
