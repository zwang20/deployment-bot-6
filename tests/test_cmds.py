"""
test_cmds.py

tests functions in the cmds module
"""

import pytest
import cmds
import error
import cmessage

pytestmark = pytest.mark.anyio

async def test_echo():
    """
    tests cmds.echo
    """

    # no arguments
    with pytest.raises(error.ArgumentRequiredError):
        assert await cmds.echo(cmessage.Message())

    # normal usage
    assert await cmds.echo(cmessage.Message(), *["Test"]) == "`Tester#1234:` Test"

async def test_ping():
    """
    tests cmds.ping
    """

    # no arguments
    with pytest.raises(error.ArgumentRequiredError):
        assert await cmds.ping(cmessage.Message())

    # too many arguments
    with pytest.raises(error.UnknownArgumentError):
        assert await cmds.ping(cmessage.Message(), *["1", "2"])

    # normal usage
    assert await cmds.ping(cmessage.Message(), *["google.com"])

async def test_time():
    """
    tests cmds.time
    """

    # no arguments
    assert await cmds.time(cmessage.Message())

    # too many arguments
    with pytest.raises(error.UnknownArgumentError):
        assert await cmds.time(cmessage.Message(), *["1", "2"])

    # unknown timezone
    with pytest.raises(error.TimezoneNotFoundError):
        assert await cmds.time(cmessage.Message(), *["1"])

    # normal usage
    assert await cmds.time(cmessage.Message(), *["America/New_York"])

async def test_ver():
    """
    tests cmds.ver
    """

    # no arguments
    assert await cmds.ver(cmessage.Message())

    # too many arguments
    with pytest.raises(error.UnknownArgumentError):
        assert await cmds.ver(cmessage.Message(), *["1"])

async def test_help():
    """
    tests cmds.help
    """

    # no arguments
    with pytest.raises(FileNotFoundError):
        assert await cmds.chelp(cmessage.Message())

    # too many arguments
    with pytest.raises(error.UnknownArgumentError):
        assert await cmds.chelp(cmessage.Message(), *["1", "2"])

    # unknwon help
    with pytest.raises(error.HelpNotFoundError):
        assert await cmds.chelp(cmessage.Message(), *["1"])

async def test_invite():
    """
    tests cmds.invite
    """

    # no arguments
    assert await cmds.invite(cmessage.Message())

    # too many arguments
    with pytest.raises(error.UnknownArgumentError):
        assert await cmds.invite(cmessage.Message(), *["1", "2"])

    # normal usage
    with pytest.raises(FileNotFoundError):
        assert await cmds.invite(cmessage.Message(), *["1"])
