"""
ver.py

includes ver
"""

from version import version


async def ver(message, *args):
    # pylint:disable=unused-argument
    """
    ver

    returns formated version and date of update
    """

    with open('date.txt', 'r', encoding="utf-8") as file:
        return f"""```version:{'v'+version} \nupdated: {file.read()}```"""
