"""
calc.py

contains calc
"""

import urllib.parse
import error

async def calc(*args):
    """
    calc

    "calculates" the given arguments
    """

    # fix args
    args = args[1:]

    # check if there are any arguments
    if not args:
        raise error.ArgumentRequiredError

    # return output
    return f"https://www.google.com.au/search?q={urllib.parse.quote(' '.join(args))}"
