"""
dice.py

implements the dice command
"""

import random
from error import ArgumentRequiredError, UnknownArgumentError

async def dice(*args):
    """
    dice()

    rolls dice
    """

    # fix args
    args = args[1:]

    # check for argument
    if len(args) == 0:
        raise ArgumentRequiredError
    if len(args) > 1:
        raise UnknownArgumentError

    # get dice
    dice_x = int(args[0].split('d')[0])
    dice_y = int(args[0].split('d')[1])

    # check dice
    assert 0 < dice_x < 100
    assert 0 < dice_y < 100

    # roll dice
    dies = [random.randint(1, dice_y) for _ in range(dice_x)]

    # print result
    string = "\n".join([
        f"dice: {dies}",
        f"sum:  {sum(dies)}",
        f"min:  {min(dies)}",
        f"max:  {max(dies)}",
        f"avg:  {sum(dies) / len(dies)}",
    ])

    # return result
    return f"```{string}```"
