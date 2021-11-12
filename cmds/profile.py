"""
profile.py

includes profile()
"""

import error

async def profile(message, *args):
    """
    profile()

    Profile a user.
    """

    # check args
    if args:
        raise error.UnknownArgumentError

    # get profile
    string = '\n'.join([
        f"Name: {message.author}",
        f"ID: {message.author.id}",
        f"Created at: {message.author.created_at}",
        f"Bot: {message.author.bot}",
        f"System: {message.author.system}"
    ])
    return f"```{string}```"

async def avatar(message, *args):
    """
    avatar()

    Get a user's avatar.
    """

    # check args
    if args:
        raise error.UnknownArgumentError

    # get avatar
    return f"{message.author.avatar_url}"
