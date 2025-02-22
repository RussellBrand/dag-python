

from typing import NamedTuple


type NodeName = str


class Tree(NamedTuple):
    roots: list[NodeName]
    nodenames: set[NodeName]
    connections: dict[NodeName, set[NodeName]]


def nodes(tree: Tree) -> set[NodeName]:
    return tree.nodenames


def graph_copy(tree: Tree) -> Tree:
    return Tree([], nodes(tree), {})


def graph_equal(tree1: Tree, tree2: Tree) -> bool:
    if nodes(tree1) != nodes(tree2):
        return False
    if edges(tree1) != edges(tree2):
        return False
    return True


def edges(tree: Tree) -> set[tuple[NodeName, NodeName]]:
    return set((node, child) for node in tree.connections for child in tree.connections[node])


def MakeTree(roots: list[NodeName], nodenames: list[NodeName], connections: dict[NodeName, set[NodeName]]) -> Tree:
    return Tree(roots, set(nodenames), connections)


def ignore(*_junk) -> None:  # type: ignore
    if _junk:
        pass


def is_tree(tree: Tree) -> bool:
    if len(tree.roots) != 1:
        return False
    return True
