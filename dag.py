

from typing import NamedTuple


type NodeName = str


class Tree(NamedTuple):
    roots: list[NodeName]
    # finals: list[NodeName]
    nodenames: set[NodeName]
    connections: dict[NodeName, list[NodeName]]


def nodes(tree: Tree) -> set[NodeName]:
    return tree.nodenames


def graph_copy(tree: Tree) -> Tree:
    return Tree([], nodes(tree), {})


def graph_equal(tree1: Tree, tree2: Tree) -> bool:
    return nodes(tree1) == nodes(tree2)


def MakeTree(roots: list[NodeName], nodenames: list[NodeName], connections: dict[NodeName, list[NodeName]]) -> Tree:
    return Tree(roots, set(nodenames), connections)


def ignore(*_junk) -> None:  # type: ignore
    if _junk:
        pass


def is_tree(tree: Tree) -> bool:
    if len(tree.roots) != 1:
        return False
    return True
