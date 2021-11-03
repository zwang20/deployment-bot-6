"""
client

includes variables important to the function of the bot
"""
#pylint:disable=global-at-module-level
#pylint:disable=invalid-name

import asyncio

import discord

global loop
loop = asyncio.new_event_loop()

global BOT_STATUS
BOT_STATUS = False

global DEBUG_STATUS
DEBUG_STATUS = True

global client
client = discord.Client(loop=loop)
