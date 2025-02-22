# import pytest
from dag import MakeTree, Tree, graph_copy, graph_equal, is_tree, nodes

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

# copy


def test_copy_of_empty_tree_has_same_of_nodes() -> None:
    original = MakeTree([], [], {})
    the_copy: Tree = graph_copy(original)
    assert (nodes(original) == nodes(the_copy))


def test_equal_graphs_have_same_nodes() -> None:
    original = MakeTree(['a'], ['a', 'b', 'c'], {'a': ['b', 'c']})
    different_order = MakeTree(['a'], ['b', 'a', 'c'], {'a': ['b', 'c']})
    assert (graph_equal(original, different_order))


def test_equal_graphs_need_same_nodes() -> None:
    original = MakeTree(['a'], ['a', 'b', 'c', 'd'], {'a': ['b', 'c']})
    different_order = MakeTree(['a'], ['b', 'a', 'c'], {'a': ['b', 'c']})
    assert (not (graph_equal(original, different_order)))


def test_equal_graphs_have_same_edges() -> None:
    original = MakeTree(['a'], ['a', 'b', 'c'], {'a': ['b', 'c']})
    different_order = MakeTree(['a'], ['a', 'b', 'c'], {'a': ['c', 'b']})
    assert (graph_equal(original, different_order))
