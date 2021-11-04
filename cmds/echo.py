"""
echo.py

contains echo() and echoa()
"""

import datetime
import error
import database

async def echo(message, *args):
    """
    echo()

    echos message
    """

    # check for arguments:
    if args:
        return f"`{message.author}:` {' '.join(args)}"

    raise error.ArgumentRequiredError

async def echoa(message, *args):
    """
    echoa()

    echos message anonymously
    """

    # get admins from database
    admins = database.get("admins")

    # check for priviledges
    if any([
        str(message.author.id) in admins,
        message.channel.permissions_for(message.author).administrator,
    ]):

        if args:
            database.write("echoa", str(message.id), string='\n'.join([
                f"{datetime.datetime.now()}",
                f"{message.channel.id}: {message.channel.name}",
                f"{message.author.id}: {message.author}",
                f"{' '.join(args)}",
            ]))
            return ' '.join(args)

        raise error.ArgumentRequiredError

    raise error.AuthorisationError
