"""
invite.py

contains invite()
"""

from database import get
import error

async def invite(*args):
    """
    invite()

    returns the invite link to the bot or the server
    """

    # fix args
    args = args[1:]

    # check if args are empty
    if len(args) == 0:
        link = (
            "https://discordapp.com/api/oauth2/"
            "authorize?client_id=681294773629485071&permissions=8&scope=bot"
        )
        return link

    # check for extra args
    if len(args) > 1:
        raise error.UnknownArgumentError

    # get invite link
    return get("invites", args[0])[0]
