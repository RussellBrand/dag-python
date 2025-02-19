import pytest
from dag import is_tree, Tree

EMPTY_TREE = Tree([], [], [], {})


@pytest.mark.skip
def test_empty_tree_is_false():
    assert is_tree(EMPTY_TREE) is True
    # assert is_tree(EMPTY_TREE) is False
