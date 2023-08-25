from checker import Checker


def test_constructor():
    c = Checker(1, 2, "human", "red", "8", "king_image")
    assert c.x == 1
    assert c.y == 2
    assert c.player == "human"


def test_move():
    c = Checker(1, 2, "human", "red", "8", "king_image")
    c.move(3, 4)
    assert c.x == 3
    assert c.y == 4


def test_is_king():
    c = Checker(1, 2, "human", "red", "8", "king_image")
    assert not c.is_king


def test_set_to_king():
    c = Checker(1, 2, "human", "red", "8", "king_image")
    c.set_to_king()
    assert c.is_king
