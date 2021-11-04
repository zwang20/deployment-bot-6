"""
database.py

contains sync()
"""

from database import get, write
from error import AuthorisationError

async def dwrite(message, *args):
    """
    write()

    writes string to file if user is admin
    """

    # get admins from database
    admins = get("admins")

    # check for priviledges
    if str(message.author.id) in admins:

        # write
        write(*(args[0].split('.')), string=' '.join(args[1:]))

        return "Data written"

    raise AuthorisationError
