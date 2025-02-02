"""
Module for creating command line interface.
"""

from pathlib import Path
from argparse import ArgumentParser

import config


def parse_args():
    """
    Function to create a command line tool using the standard `argparse` library.
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
    parser.add_argument(
        "-r",
        "--recheck-timer",
        dest="recheck_timer",
        type=int,
        default=config.DEFAULT_RECHECK_TIMER,
        help="seconds before rechecking plugins",
    )

    return parser.parse_args()
