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

    # Commenting out insertion methods: add() and heapify_up()

    def __heapify_down(self, index: Optional[int] = 0):
        """Move root to proper position in heap"""
        if index >= len(self.nodes) or not self.__has_left_child(index):
            return self.nodes
        # Check if greater than left or right
        smaller_child_idx = self.__get_left_child_index(index)
        if self.__has_right_child(index) and \
                self.__right_child(index) < self.__left_child(index):
            smaller_child_idx = self.__get_right_child_index(index)

        if self.nodes[index] < self.nodes[smaller_child_idx]:
            # Lower than both, do nothing
            return self.nodes

        if self.nodes[index] > self.nodes[smaller_child_idx]:
            # Swap with smaller child
            self.__swap(index, smaller_child_idx)
            return self.__heapify_down(smaller_child_idx)

    def poll(self) -> Optional[int]:
        """
        Polls lowest element from the heap (usually root). To avoid memory shift
        of first-element removal, we copy the last element to the first
        position, shrink the size by 1 and heapify down.
        """
        if self.is_empty():
            print('Empty, not polling')
            return None

        # Remove first and insert the last one added as the root
        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        # Shrink size by 1
        # Could've also used self.nodes = self.nodes[:-1]
        del self.nodes[-1]

        self.__heapify_down()
        return removed_node
