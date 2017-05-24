def sort(array):

    for j in range(len(array)):
        x = array.index(min(array[j:]))
        array[x], array[j] = array[j], array[x]

    return array
