import pytest

from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()


def test_sguare_positiv(simple_math):
    res = simple_math.square(2)
    assert res == 4


def test_sguare_pos_float(simple_math):
    res = simple_math.square(4.0)
    assert res == 16


def test_sguare_null(simple_math):
    res = simple_math.square(0)
    assert res == 0


def test_sguare_negativ(simple_math):
    res = simple_math.square(-3)
    assert res == 9


def test_cube_positiv(simple_math):
    res = simple_math.cube(3)
    assert res == 27


def test_cube_negativ(simple_math):
    res = simple_math.cube(-3)
    assert res == -27


def test_cube_null(simple_math):
    res = simple_math.cube(0)
    assert res == 0


def test_cube_float(simple_math):
    res = simple_math.cube(3.0)
    assert res == 27.0


def test_cube_float_neg(simple_math):
    res = simple_math.cube(-3.0)
    assert res == -27