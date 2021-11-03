"""
echo.py

contains echo() and echoa()
"""

import error


async def echo(message, *args):
    """
    echo()

    echos message
    """

    # check for arguments:
    if args:
        return f"`{message.author}:` {' '.join(args)}"

    raise error.ArgumentRequiredError
