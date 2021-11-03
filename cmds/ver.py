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

    with open('date.txt', 'r', encoding="utf-8") as date:
        with open("data.txt", "r", encoding="utf-8") as data:
            output = '\n'.join([
                f'Discord bot version:   {version}',
                f'Last updated:          {date.readline()}',
                f'Database last updated: {data.readline()}',
            ])
            return f'```{output}```'
