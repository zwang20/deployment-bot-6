"""
others.py

includes misc. commands
"""

import error

def wow(message, *args):
    """
    wow()

    returns wow @user
    """

    # check for args
    if len(args) > 0:
        raise error.UnknownArgumentError

    # return wow
    return "wow <@{}>".format(message.author.id)
