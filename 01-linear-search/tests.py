#!/usr/bin/env python
from main import locate_cards

def test_empty():
    inp = []
    out = locate_cards(inp, 3)
    assert out == -1


def test_1():
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    out = locate_cards(inp, 3)
    assert out == 2


def test_2():
    inp = [3, 8, 9, 11, 16, 22]
    out = locate_cards(inp, 22)
    assert out == 5


def test_3():
    inp = [0, 1, 3, 4, 7, 10, 11, 13]
    out = locate_cards(inp, 1)
    assert out == 1


def test_4():
    inp = [-1, 1, 2, 4]
    out = locate_cards(inp, 4)
    assert out == 3


def test_5():
    inp = [-127, -9, -1, 3]
    out = locate_cards(inp, -127)
    assert out == 0


def test_6():
    inp = [6]
    out = locate_cards(inp, 6)
    assert out == 0


def test_7():
    inp = [-9, 2, 5, 7, 9]
    out = locate_cards(inp, 4)
    assert out == -1


def test_8():
    inp = [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 8, 8]
    out = locate_cards(inp, 3)
    assert out == 6


def test_9():
    inp = [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 8, 8]
    out = locate_cards(inp, 6)
    assert out == 7
