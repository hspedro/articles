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

    def __len__(self) -> int:
        return len([node for node in self]) - 1

    def __contains__(self, data: Any) -> bool:
        for node in self:
            if node.data == data:
                return True
        return False

    def __str__(self) -> str:
        node = self.HEAD
        nodes = []
        for node in self:
            nodes.append(str(node))
        nodes.append('None')
        return ' -> '.join(nodes)

    def __getitem__(self, index: int) -> SLLNode:
        if index < 0 and index > len(self) - 1:
            raise IndexError(f'Index {index} out of range')

        node = self.HEAD
        for _ in range(index):
            node = node.next
        return node.next

    def __setitem__(self, index: int, data: Any) -> SinglyLinkedList:
        if index < 0 and index > len(self) - 1:
            raise IndexError(f'Index {index} out of range')

        node = self.HEAD
        for _ in range(index + 1):
            node = node.next
        node.data = data
        return self

    def __delitem__(self, index: int):
        if index < 0 and index > len(self) - 1:
            raise IndexError(f'Index {index} out of range')

        node = self.HEAD
        for _ in range(index):
            node = node.next
        node.next = node.next.next if node.next else None
        return

    def __gt__(self, other: SinglyLinkedList) -> bool:
        if len(self) > len(other):
            return True

    def __lt__(self, other: SinglyLinkedList) -> bool:
        if len(self) < len(other):
            return True

    def __ge__(self, other: SinglyLinkedList) -> bool:
        if len(self) >= len(other):
            return True

    def __le__(self, other: SinglyLinkedList) -> bool:
        if len(self) <= len(other):
            return True

    def __eq__(self, other: SinglyLinkedList) -> bool:
        if len(self) != len(other):
            return False
        for node in self:
            if node.data != other[node.data]:
                return False
        return True

    def __ne__(self, other: SinglyLinkedList) -> bool:
        return not self == other

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

    def find(self, data: Any) -> Optional[SLLNode]:
        if self.HEAD.next is None:
            return None

        for node in self:
            if node.data == data:
                return node

    def remove(self, data: Any) -> SinglyLinkedList:
        if self.HEAD.next is None:
            return None

        for node in self:
            if node.next.data == data:
                node.next = node.next.next
                return self
