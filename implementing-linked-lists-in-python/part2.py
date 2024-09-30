from __future__ import annotations
from typing import Any, List, Optional


class SLLNode:
    def __init__(self, data: Any, next: Optional[SLLNode] = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}"


class SinglyLinkedList:
    """ Custom implementation of a Singly-Linked List"""

    def __init__(self, nodes: Optional[List[SLLNode]] = None):
        # Note: the HEAD node will only contain data as 'HEAD' to
        # print the list. See: __repr__()
        self.HEAD = SLLNode('HEAD', next=None)
        if nodes is not None:
            for node in nodes:
                self.append(node.data)

    def __iter__(self):
        node = self.HEAD
        while node is not None:
            yield node
            node = node.next
