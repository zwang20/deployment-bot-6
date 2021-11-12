"""
help.py

contains chelp()
"""

from database import get
import error


async def chelp(*args):
    """
    chelp()

    stands for command help

    returns string for verb
    """

    # fix args
    args = args[1:]

    # check args
    if len(args) > 1:
        raise error.UnknownArgumentError

    if args:
        try:
            string = '\n'.join(get("helps", args[0]))
        except FileNotFoundError as err:
            raise error.HelpNotFoundError from err

    else:
        string = '\n'.join(get("help"))

    return f"```{string}```"
