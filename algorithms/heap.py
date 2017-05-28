# creating a representation for infinity.
inf = float("inf")


def get_largest_child(parent, array, array_size):
    """Given a parent node, returns its largest child. If None is found returns (-infinity, None)."""

    left = parent * 2 + 1
    right = parent * 2 + 2
    left_value = right_value = -inf

    if left >= array_size:
        left = None
    else:
        left_value = array[left]

    if right >= array_size:
        right = None
    else:
        right_value = array[right]

    if left_value > right_value:
        return left_value, left
    else:
        return right_value, right


def max_heapify(array):
    """Transforms an array into a max-heap."""
    n = len(array)

    def recursive_max_heapify(parent):
        largest_child, child_index = get_largest_child(parent, array, n)

        # just heapify this node if it has children
        if child_index and largest_child > array[parent]:
            array[parent], array[child_index] = array[child_index], array[parent]
            return recursive_max_heapify(child_index)

    for i in range(n // 2, -1, -1):
        recursive_max_heapify(i)


def update_heap(parent, heap, heap_size):
    """Moves the top element on the heap to its proper position."""
    largest, child_index = get_largest_child(parent, heap, heap_size)

    if child_index and largest > heap[parent]:
        heap[parent], heap[child_index] = heap[child_index], heap[parent]
        return update_heap(child_index, heap, heap_size)

    return heap


def sort(array):
    n = len(array)

    max_heapify(array)

    for i in range(n):
        # swapping the heap's head (largest element) with its tail (random element).
        array[0], array[n - i - 1] = array[n - i - 1], array[0]

        # updating heap to have the largest element atop
        array = update_heap(0, array, n-i-1)

    return array


