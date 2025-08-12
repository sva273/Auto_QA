import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_sum(calculator):
    res = calculator.sum(4, 5)
    assert res == 9


def test_sum_1(calculator):
    res = calculator.sum(-5, -9)
    assert res == -14


def test_sum_2(calculator):
    res = calculator.sum(-3, 3)
    assert res == 0


def test_sum_3(calculator):
    res = calculator.sum(2.6, 1.3)
    res = round(res, 1)
    assert res == 3.9
