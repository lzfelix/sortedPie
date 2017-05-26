from .quick import partition


def sort(array, use_median=False):

    queue = list()
    queue.append((0, len(array)))

    while queue:
        start, end = queue.pop()
        p = partition(array, start, end, use_median)

        if p - start > 1:
            queue.append((start, p))

        p += 1
        if end - p > 1:
            queue.append((p, end))

    return array
