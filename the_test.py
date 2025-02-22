# import pytest
from dag import MakeTree, Tree, is_tree

EMPTY_TREE: Tree = MakeTree([], [], {})

# is_tree


def test_empty_graph_is_not_a_tree():
    assert is_tree(EMPTY_TREE) is False


def test_graph_win_exactly_one_root_is_a_tree():
    assert (is_tree(MakeTree(['a'], ['a'], {})))
    assert (is_tree(MakeTree(['a'], ['a', 'b', 'c'], {})))
    assert (
        is_tree(MakeTree(['a'], ['a', 'b', 'c', 'd'], {'a': ['b', 'c', 'd']})))


def test_graph_with_multiple_roots_is_not_a_tree():
    assert not is_tree(MakeTree(['a', 'b'], ['a', 'b'], {}))

#
