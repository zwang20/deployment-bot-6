# pylint:disable=logging-fstring-interpolation
"""
main.py

the main script for the program
run `py main.py` on windows or
`python3 main.py` for other os
"""
import logging
import datetime
# import multiprocessing
# import subprocess
# import asyncio
# import os

import discord
# import discord_slash

import env
import client

logging.basicConfig(level=logging.INFO)
# logging.debug(f"\t{datetime.datetime.now()}")
# logging.info(f"\t{datetime.datetime.now()}")
# logging.warning(f"\t\033[33m{datetime.datetime.now()}\033[0m")
# logging.error(f"\t\033[31m{datetime.datetime.now()}\033[0m")
# logging.critical(f"\t\033[41m{datetime.datetime.now()}\033[0m")


def main():
    """
    main()

    main function of the program
    """
    # firebase = pyrebase.initialize_app(env.config)
    # db = firebase.database()
    logging.info(
        f"\t{datetime.datetime.now()} main starting with discord version {discord.__version__}"
    )

    client.client.run(env.token)  # Start bot
    # Nothing will run after that


if __name__ == '__main__':
    main()
