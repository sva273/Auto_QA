import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1,2,3),
        (-1, -4, -5),
        (5, -2, 3),
        (-1,5, 4),
        (0.8, 1.2, 2.0)
    ]
)

def test_sum(calculator, a, b, expected):
    res = calculator.sum(a, b)
    assert res == expected

