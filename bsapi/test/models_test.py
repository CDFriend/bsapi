import pytest
from bsapi.models import *


def test_startresponse():
    """StartResponse should set a color attribute."""
    color = "#FFOOFF"
    resp = StartResponse(color)
    assert resp["color"] == color


def test_startresponse_bad():
    """StartResponse should throw exception if not given a string."""
    with pytest.raises(AssertionError):
        StartResponse(11)


@pytest.mark.parametrize("move", ['up', 'down', 'left', 'right'])
def test_moveresponse(move):
    """MoveResponse should set a move attribute."""
    resp = MoveResponse(move)
    assert resp["move"] == move


def test_moveresponse_bad():
    """MoveResponse should raise an exception if not given a valid direction.
    """
    with pytest.raises(AssertionError):
        MoveResponse("THIS IS WRONG")
