# backlog

## features

graph-copy

graph-equal

add-node

- should fail on trees

add-node-with-parent

add-edge

- has to do computation on trees

- has to do computation on acyclic

remove-node

- should fail on non-leaf notes for trees

remove-link

make-frozen-copy

- has to do computation for trees

depth

- how do we handle multiple roots

- how do we handle cyclics

descendents (iterable)

- depth first or breadth first

ancestors (iterable)

- depth first or breadth first

step-count-from-to(node, node)

is-tree

is-acyclic

to-s

- should this be guaranteed ordering?

to-repr

- should this be guaranteed ordering?

python style load

load-from-repr

is-empty

- #nodes is zero

is-path

path-from-to

is-in-acycle

- should always be false for trees

various make froms

nodes (iterable)

edges (iterable)

connections (iterable)

## refactoring

better representation

- do we need "finals" at all

- collapse roots, nodes, edges -> dict

- dict should be to-set rather than to-list

make modifiable

## pytest maintenance

don't call make tuple directly

rather than having global constants for sample data, have functions that make them each time

was-modified

make-unique-node-name

@param's

pytest support in vscode

running make in vscode

watch mode

## python maintenance

python version -> file

pretty print on save

## git maintance

before commit hook to run the test

## done

## inbox

do we want to make this a class?
