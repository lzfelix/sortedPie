def sort(array):

    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break

    return array
