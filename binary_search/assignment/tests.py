from main import get_rotations


def test_empty():
    inp = []
    out = get_rotations(inp)
    assert out == -1


def test_1():
    inp = [5, 0, 1, 2, 4]
    out = get_rotations(inp)
    assert out == 1


def test_2():
    inp = [5, 0, 1, 2, 4, 5]
    out = get_rotations(inp)
    assert out == 1


def test_3():
    inp = [0, 1, 2, 4, 5]
    out = get_rotations(inp)
    assert out == 0


def test_4():
    inp = [1, 2, 4, 7, -5, -3, 0]
    out = get_rotations(inp)
    assert out == 4
