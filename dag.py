

from typing import NamedTuple


type NodeName = str


class Tree(NamedTuple):
    roots: list[NodeName]
    finals: list[NodeName]
    nodenames: list[NodeName]
    edges: dict[NodeName, list[NodeName]]


def ignore(*_junk) -> None:  # type: ignore
    if _junk:
        pass


def is_tree(_tree: Tree) -> bool:
    ignore(_tree)
    if len(_tree.roots) != 1:
        return False
    return True
