from typing import List, Optional


class MinHeap:
    nodes: List[int]

    def __init__(self, nodes: List[int] = []):
        self.nodes = []
        for node in nodes:
            self.add(node)

    # Helper methods defined previously:
    # __get_left_child_index
    # __get_right_child_index
    # __get_parent_index
    # ...

    def __swap(self, first_idx: int, second_idx: int):
        if first_idx >= len(self.nodes) or second_idx >= len(self.nodes):
            print(f'first ({first_idx}) or second ({second_idx}) are invalid')
            return
        tmp = self.nodes[first_idx]
        self.nodes[first_idx] = self.nodes[second_idx]
        self.nodes[second_idx] = tmp

    def __heapify_up(self, child: Optional[int] = None):
        """Move last added element to correct position in heap"""
        if not child:
            # Start with last
            child = len(self.nodes) - 1
        # Check if smaller than parent
        parent_idx = self.__get_parent_index(child)
        if self.__parent(child) and self.nodes[child] < self.__parent(child):
            # Swap child <> parent
            self.__swap(child, parent_idx)
            # Recurse on parent index now (should have child value)
            self.__heapify_up(child=parent_idx)
        # If its not smaller, leave as it is
        return self.nodes

    def add(self, item: int):
        self.nodes.append(item)
        self.__heapify_up()
