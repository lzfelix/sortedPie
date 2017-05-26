def sort(array):
    if len(array) == 1:
        return array

    middle = len(array) // 2
    left = sort(array[:middle])
    right = sort(array[middle:])

    k = 0
    li, ri = 0, 0
    ll = len(left)
    lr = len(right)

    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            array[k] = left[li]
            li += 1
        else:
            array[k] = right[ri]
            ri += 1

        k += 1

    while li < len(left):
        array[k] = left[li]
        li += 1
        k += 1

    while ri < len(right):
        array[k] = right[ri]
        ri += 1
        k += 1

    return array
