"""
write.py

contains write
"""

import os


def write(*args, **kwargs):
    """
    write()

    writes string to file
    """

    with open(os.path.join(*(["db-database"]+list(args))), 'w', encoding="utf-8") as file:
        file.write(kwargs["string"])
