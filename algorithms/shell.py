from .insertion import sort as insertion_sort


def sort(array):
    # for details and other sequences, see: Sedgewick, Robert. "Analysis of Shellsort and related algorithms."
    # European Symposium on Algorithms. Springer Berlin Heidelberg, 1996.
    leap_sizes = [2**x-1 for x in range(10,0,-1)]

    for leap in leap_sizes:
        array = insertion_sort(array, leap)

    return array
