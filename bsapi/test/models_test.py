import pytest
import random
from bsapi.models import *


def test_coords():
    """Coords should set an x and y parameter."""
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    data = {"x": x, "y": y}

    coords = Coords(data)

    assert coords.x == x
    assert coords.y == y


def test_snake():
    data = {
        "id": "snake-id-string",
        "name": "Sneky Snek",
        "health": 90,
        "body": [
          { "x": 1, "y": 3 },
          { "x": 2, "y": 4 },
        ]
    }

    snake = Snake(data)

    assert snake.id == "snake-id-string"
    assert snake.name == "Sneky Snek"
    assert snake.health == 90
    assert snake.head().x == 1 and snake.head().y == 3


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
