def sort(array):

    for i in range(len(array)):
        search_array = array[i:]

        x = search_array.index(min(search_array))
        array[x+i], array[i] = array[i], array[x+i]

    return array
