"""
emote.py

contains emote()
"""

import client
import error

async def emote(*args):
    """
    emote()

    returns the emote
    """

    # fix args
    args = args[1:]

    # check args
    if len(args) == 0:
        raise error.ArgumentRequiredError

    if len(args) > 1:
        raise error.UnknownArgumentError

    # return output
    return [
        inner for outer in [
            guild.emojis for guild in client.client.guilds
        ] for inner in outer if inner.name == args[0]
    ][0]
