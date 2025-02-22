# import pytest
from dag import is_tree, Tree

EMPTY_TREE = Tree([], [], [], {})


def test_empty_graph_is_not_a_tree():
    assert is_tree(EMPTY_TREE) is False


def test_graph_win_exactly_one_root_is_a_tree():

    assert (is_tree(Tree(['a'], [], ['a'], {})))
    assert (is_tree(Tree(['a'], [], ['a', 'b', 'c'], {})))
