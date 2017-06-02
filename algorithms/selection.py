def sort(array):

    for i in range(len(array)):
        search_array = array[i:]

        imin, tmin = i, array[i]

        for j in range(i, len(array)):
            if tmin > array[j]:
                imin, tmin = j, array[j]

        x = imin
        # x = search_array.index(min(search_array))
        array[x], array[i] = array[i], array[x]

    return array
