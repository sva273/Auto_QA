import pytest
from practik import Tree

@pytest.fixture
def tree():
    return Tree()

@pytest.mark.parametrize(
    "bulbs_sequence, expected_length",
    [
        ([1, 2, 3, 4, 5], 4),
        ([1, 4, 2, 3, 5], 8),
        ([5, 5, 5], 0),
        ([10, 1], 9),
        ([1], 0),
        ([], 0),
    ]
)

def test_garland_length(bulbs_sequence, expected_length):
    tree = Tree()
    assert tree.garland_length(bulbs_sequence) == expected_length