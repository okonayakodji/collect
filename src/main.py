"""
Program for collecting daily bonuses, configured by .yaml file.
"""

import logging
import pprint
from sys import exit as sys_exit

import config
from cli import parse_args
from collect import Collect


def main():
    """
    App entrypoint
    """

    args = parse_args()

    logging.basicConfig(
        format=config.LOGGING_FORMAT,
        level=(logging.DEBUG if args.debug else logging.INFO),
    )

    logging.debug(_ := f"parsed cli arguments\n{pprint.pformat(vars(args))}")

    try:
        app = Collect(args.config, logging.getLogger(__name__)).with_parsed_config()
        app.run(args.recheck_timer)
    except ValueError:
        logging.error("Invalid file extension. Should be .yaml or .yml")
        sys_exit()

    logging.debug(_ := f"fields of created app\n{app}")


if __name__ == "__main__":
    main()
