"""
ping.py

contains ping()
"""

import os
import subprocess
import error

async def ping(message, *args):
    # pylint:disable=unused-argument
    """
    ping()

    pings website
    """

    # check for excess args:
    if len(args) > 1:
        raise error.UnknownArgumentError

    # check for args
    if not args:
        raise error.ArgumentRequiredError

    # if windows
    if os.name == "nt":
        output = subprocess.run(
            ["ping", args[0]],
            check=True,
            stdout=subprocess.PIPE
        ).stdout

    # if unix
    else:
        output = subprocess.run(
            ["ping", "-c", "4", args[0]],
            check=True,
            stdout=subprocess.PIPE
        ).stdout

    # return
    return f"""```{output}```"""
