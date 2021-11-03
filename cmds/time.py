"""
time.py

contains time()
"""

import datetime
import pytz

import error


async def time(message, *args):
    """
    time()

    returns time at timezone
    """

    # checks for excess arguments
    if len(args) > 1:
        raise error.UnknownArgumentError

    # checks for argument
    if len(args) == 1:

        # checks timezone
        if args[0] not in pytz.all_timezones:
            raise error.TimezoneNotFoundError

        # sets timezone
        timezone = args[0]

    else:
        # sets default timezone
        timezone = 'UTC'

    # returns output
    return datetime.datetime.now(pytz.timezone(timezone)).strftime("%A %Y %B %d %H:%M:%S %Z %z")
