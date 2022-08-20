#!/usr/bin/python3
"""
Binary Search tree generator v1.0
"""
import random
from typing import Optional, List


class BaseNode:  # Basically Root
    def __init__(self, data: int):
        self.data: int = data
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

    def is_leaf(self):
        return self.left_child is None and self.right_child is None


class Node(BaseNode):
    def __init__(self, data: int, parent: BaseNode):
        super().__init__(data)
        self.parent: BaseNode = parent

    @property
    def children(self):
        return list(filter(None, [self.left_child if self.left_child else None,
                                  self.right_child if self.right_child else None]))


class BST(BaseNode):
    def __init__(self, _in: List[int]):
        super().__init__(_in[0])
        self._in = _in
        self.generate_tree()

        # Graphics
        self.unit_dist = "\t\t\t"

    @property
    def depth(self) -> int:
        depths = []

        return max(depths)

    def get_line(self, lvl: int) -> List[Node]:
        assert lvl <= self.depth
        row = [self]
        _buff = []
        for i in range(lvl):
            for node in row:
                _buff.extend([node.left_child, node.right_child])
            row = list(filter(None, _buff))
        return row

    def generate_tree(self):
        list(map(self.insert, self._in))  # Fucking iterators

    def insert(self, data: int, root: BaseNode = None) -> None:
        if root is None:
            root = self
        if root.data > data:
            if root.left_child is None:
                root.left_child = Node(data, root)
            self.insert(data, root.left_child)
        elif root.data < data:
            if root.right_child is None:
                root.right_child = Node(data, root)
            self.insert(data, root.right_child)

    def search(self, data: int, root: BaseNode = None):
        if root is None:
            root = self

        if data < root.data:
            print("left")
            self.search(data, root.left_child)
        elif data > root.data:
            print("right")
            self.search(data, root.right_child)
        elif data == root.data:
            print(root)
            return root

    def delete(self, data: int):
        pass

    def show(self):
        pass


if __name__ == '__main__':
    bst = BST([random.randint(13, 15) for i in range(150)])
    a = bst.search(13)  # BRUH why bruuuuuuuuuuuuuuuh
