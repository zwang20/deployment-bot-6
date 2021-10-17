"""
ping.py

contains ping()
"""

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

    # return
    return f"""```{subprocess.check_output(["ping", args[0], "-c", "5"]).decode()}```"""
