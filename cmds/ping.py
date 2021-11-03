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
        output = subprocess.check_output(["ping", args[0]]).decode()

    # if unix
    else:
        output = subprocess.check_output(["ping", "-c", "4", args[0]]).decode()

    # return
    return f"""```{output}```"""
