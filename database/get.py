"""
get.py

contains get
"""

import os


def get(*args):
    """
    get(*args)

    retrieves data from database with args as path
    """

    with open(os.path.join(*(["db-database"]+list(args))), 'r', encoding="utf-8") as file:
        return file.read().splitlines()
