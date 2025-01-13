"""
Module for creating command line interface
"""

from pathlib import Path
from argparse import ArgumentParser

import config


def parse_args():
    """
    TODO
    """

    parser = ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="enable debug mode")
    parser.add_argument(
        "config",
        nargs="?",
        type=Path,
        default=Path(config.DEFAULT_PATH_TO_CONFIG),
        help=f'path to config. default: "{config.DEFAULT_PATH_TO_CONFIG}"',
    )

    return parser.parse_args()
