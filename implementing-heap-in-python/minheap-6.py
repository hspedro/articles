from typing import List


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
    # Commenting out peek() and is_empty()

    def heapify_children(self, index: int):
        """
        Heapify children of a node to obey left < right.
        """
        if not self.__has_left_child(index):
            return
        if not self.__has_right_child(index):
            return
        if self.__right_child(index) < self.__left_child(index):
            self.__swap(
                self.__get_right_child_index(index),
                self.__get_left_child_index(index))
        self.heapify_children(self.__get_left_child_index(index))
        self.heapify_children(self.__get_right_child_index(index))


def heapsort_in_place(unsorted_input: List[int]) -> List[int]:
    """ Heapsort in-place: heap.nodes is unsorted_input == True """
    heap = MinHeap()
    heap.nodes = unsorted_input
    size = len(unsorted_input)
    print(f'identity check: {heap.nodes is unsorted_input}')
    for idx in range(size // 2, -1, -1):
        heap.heapify_down(idx)
    heap.heapify_children(0)
    return heap.nodes


if __name__ == '__main__':
    unsorted_array = [10, 15, 8, 20, 17]
    print(f'heapsort in-place: {heapsort_in_place(unsorted_array)}')
    # identity check: True
    # heapsort with aux space: [8, 10, 15, 17, 20]
