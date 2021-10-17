# pylint:disable=invalid-name
# pylint:disable=global-at-module-level
"""
client

includes variables important to the function of the bot
"""

import asyncio

import discord

global loop
loop = asyncio.new_event_loop()

global BOT_STATUS
BOT_STATUS = False

global DEBUG_STATUS
DEBUG_STATUS = False

client = discord.Client(loop=loop)