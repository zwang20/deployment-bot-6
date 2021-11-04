"""
kick.py

includes kick
"""

from client import client
from database import get


async def kick(message, *args):
    """
    kick

    kicks person from guild given id
    """

    # get admins from database
    admins = get("admins")

    if any([
        message.channel.permissions_for(message.author).administrator,
        str(message.author.id) in admins,
    ]):

        if args:

            try:

                client.get_user(int(args[0])).id

            except AttributeError:

                return 'Unknown user'

            except ValueError:

                return 'User ID not found'

            await message.guild.kick(client.get_user(int(args[0])))

            return 'User <@' + str(args[0]) + '> has been kicked'

        return 'Argument <User ID> missing'
