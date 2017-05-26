def partition(array, down, up, use_median):
    if use_median:
        pivot_index = (up + down) // 2
        array[down], array[pivot_index] = array[pivot_index], array[down]

    pivot = array[down]

    down_begin = down + 1
    up_begin = up - 1

    i = down
    while True:
        for i in range(down_begin, up):
            if array[i] > pivot:
                break

        for j in range(up_begin, down - 1, -1):
            if array[j] <= pivot:
                break

        if i < j:
            array[i], array[j] = array[j], array[i]

            # this makes the up/down lookup resume from where it has left.
            down_begin = i
            up_begin = j

        else:
            array[j], array[down] = array[down], array[j]
            return j


def sort(array, use_median=False):

    def quicksort(down, up):
        if up - down <= 1:
            return

        pivot = partition(array, down, up, use_median)
        quicksort(down, pivot)
        quicksort(pivot + 1, up)

    quicksort(0, len(array))
    return array
