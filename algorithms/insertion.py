def sort(array):
    for i in range(len(array)):
        p = array[i]
        j = i
        while j >= 1 and array[j - 1] > p:
            array[j] = array[j - 1]
            j -= 1
        array[j] = p

    return array