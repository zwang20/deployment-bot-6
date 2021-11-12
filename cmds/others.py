"""
others.py

includes misc. commands
"""

import error

async def wow(message, *args):
    """
    wow()

    returns wow @user
    """

    # check for args
    if len(args) > 0:
        raise error.UnknownArgumentError

    # return wow
    return f"wow <@{message.author.id}>"


async def report(*args):
    """
    report()

    does nothing
    """

    # fix args
    args = args[1:]

    # check for args
    if len(args) > 0:
        raise error.UnknownArgumentError

    # return output
    return "https://github.com/zwang20/deployment-bot-6/issues"

async def returnf(*args):
    """
    returnf()

    does nothing
    """

    # fix args
    args = args[1:]

    # check for args
    if len(args) > 0:
        raise error.UnknownArgumentError

    # return output
    return "f"
