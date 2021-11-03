"""
ver.py

includes ver
"""

from version import version
import error

async def ver(*args):
    """
    ver

    returns formated version and date of update
    """

    # fix args
    args = args[1:]

    # check args
    if len(args) > 0:
        raise error.UnknownArgumentError

    with open('date.txt', 'r', encoding="utf-8") as file:
        return f"""```version:{'v'+version} \nupdated: {file.read()}```"""
