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


def heapsort_aux(unsorted_input: List[int]) -> List[int]:
    """ Heapsort using O(n) space """
    heap = MinHeap(unsorted_input)
    sorted_input = []
    for _ in range(len(unsorted_input)):
        sorted_input.append(heap.poll())
    print(f'identity check: {sorted_input is heap.nodes}')
    return sorted_input


if __name__ == '__main__':
    unsorted_array = [10, 15, 8, 20, 17]
    print(f'heapsort with aux space: {heapsort_aux(unsorted_array)}')
    # identity check: False
    # heapsort with aux space: [8, 10, 15, 17, 20]
