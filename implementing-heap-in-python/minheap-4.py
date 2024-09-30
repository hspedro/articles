from typing import List, Optional


class MinHeap:
    nodes: List[int]

    def __init__(self, nodes: List[int] = []):
        self.nodes = []
        for node in nodes:
            self.add(node)

    # Commenting out helper methods defined previously:
    # __get_left_child_index
    # __get_right_child_index
    # __get_parent_index
    # __swap
    # ...

    # Commenting out insertion methods: add() and heapify_up()
    # Commenting out deletion methods: poll() and heapify_down()

    def is_empty(self) -> bool:
        return not self.nodes

    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return None
        return self.nodes[0]
