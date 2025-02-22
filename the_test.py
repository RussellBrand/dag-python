import pytest
from dag import is_tree, Tree

EMPTY_TREE = Tree([], [], [], {})


def test_empty_tree_is_not_a_tree():

    assert is_tree(EMPTY_TREE) is False
