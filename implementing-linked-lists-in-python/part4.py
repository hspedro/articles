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

    def append(self, data: Any) -> SinglyLinkedList:
        node = self.HEAD
        for node in self:
            pass
        node.next = SLLNode(data)
        return self

    def pop(self) -> Optional[SLLNode]:
        if self.HEAD.next is None:
            return None

        node = self.HEAD
        while node.next.next:
            node = node.next

        removed_node = node.next
        node.next = None
        return removed_node

    def appendleft(self, data: Any) -> SinglyLinkedList:
        new_node = SLLNode(data)
        if self.HEAD.next is None:
            self.HEAD.next = SLLNode(data)
            return self

        previous_first = self.HEAD.next
        self.HEAD.next = new_node
        new_node.next = previous_first
        return self

    def popleft(self) -> SLLNode:
        if self.HEAD.next is None:
            return None

        previous_first = self.HEAD.next
        self.HEAD.next = previous_first.next
        return previous_first
