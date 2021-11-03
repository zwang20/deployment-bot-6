# pylint:disable=logging-fstring-interpolation
"""
main.py

the main script for the program
run `py main.py` on windows or
`python3 main.py` for other os
"""
import logging
import datetime
import traceback
# import multiprocessing
# import subprocess
# import asyncio
# import os

import discord
# import discord_slash

import env
import client
import version
import cmds

logging.basicConfig(level=logging.INFO)
# logging.debug(f"\t{datetime.datetime.now()}")
# logging.info(f"\t{datetime.datetime.now()}")
# logging.warning(f"\t\033[33m{datetime.datetime.now()}\033[0m")
# logging.error(f"\t\033[31m{datetime.datetime.now()}\033[0m")
# logging.critical(f"\t\033[41m{datetime.datetime.now()}\033[0m")

verbs = {
    "echo": cmds.echo,
    "ping": cmds.ping,
    "version": cmds.ver,
    "ver": cmds.ver,
    "time": cmds.time,
}

@client.client.event
async def on_ready():
    """
    on_ready()

    event handler for when the client is ready
    """
    logging.info(
        "\t %s We have logged in as %s", datetime.datetime.now(), client.client.user
    )
    logging.debug(
        "\t %s Changing discord presence"
    )
    await client.client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="servers",
        )
    )

async def process_message(message) -> list[str]:
    """
    process_message()

    processes a message
    """

    # ignore bots
    if message.author.bot:
        return []

    # t-bot
    if client.DEBUG_STATUS:
        if message.content.lower().startswith("<@596544931359883274>"):
            content = message.content.replace("<@596544931359883274>", "", 1).split()
        elif message.content.lower().startswith("<@!596544931359883274>"):
            content = message.content.replace("<@!596544931359883274>", "", 1).split()
        elif message.content.lower().startswith("t!"):
            content = message.content.replace("t!", "", 1).split()

    # d-bot
    else:
        if message.content.lower().startswith("<@681294773629485071>"):
            content = message.content.replace("<@681294773629485071>", "", 1).split()
        elif message.content.lower().startswith("<@!681294773629485071>"):
            content = message.content.replace("<@!681294773629485071>", "", 1).split()
        elif message.content.lower().startswith("d!"):
            content = message.content.replace("d!", "", 1).split()

    # return if content
    if content:
        return content

    # dms
    if isinstance(message.channel, discord.channel.DMChannel):
        return message.content.split()

@client.client.event
async def on_message(message):
    """
    on_message()

    event handler for when a message is sent
    """

    # process message
    content = process_message(message)

    # return if no message
    if not content:
        return

    # return if no command
    if len(content) < 1:
        return

    # get command
    verb = content[0].lower()
    nouns = content[1:]

    # try command
    try:
        with message.channel.typing():
            output = verbs[verb](message, nouns)
    except Exception as err:
        output = traceback.format_exc(err)

    # try to send output
    try:
        await message.channel.send(output)
    except Exception as err:
        await message.channel.send(traceback.format_exc(err))



def main():
    """
    main()

    main function of the program
    """
    logging.info(
        "\t %s main starting with discord version %s", datetime.datetime.now(), discord.__version__
    )
    logging.info(
        "\t %s main starting with bot version %s", datetime.datetime.now(), version.version
    )

    client.client.run(env.TOKEN)  # Start bot
    # Nothing will run after that


if __name__ == '__main__':
    main()
