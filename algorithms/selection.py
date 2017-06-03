def sort(array):

    for i in range(len(array)):
        imin, tmin = i, array[i]
        for j in range(i, len(array)):
            if tmin > array[j]:
                imin, tmin = j, array[j]

        x = imin
        array[x], array[i] = array[i], array[x]

    return array
