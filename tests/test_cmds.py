# pylint:disable=unused-import
# pylint:disable=missing-function-docstring
"""
test_cmds.py

tests functions in the cmds module
"""

import pytest
import anyio
import cmds
import main
import error
import cmessage

pytestmark = pytest.mark.anyio


async def test_echo_noargs():

    with pytest.raises(error.ArgumentRequiredError):
        assert await cmds.echo(cmessage.Message())


async def test_echo():

    assert await cmds.echo(cmessage.Message(), *["Test"]) == "`Tester#1234:` Test"


async def test_ping_noargs():

    # no arguments
    with pytest.raises(error.ArgumentRequiredError):
        assert await cmds.ping(None)


async def test_ping_toomanyargs():

    with pytest.raises(error.UnknownArgumentError):
        assert await cmds.ping(None, *["1", "2"])
