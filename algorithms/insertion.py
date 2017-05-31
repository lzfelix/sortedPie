
def sort(array):
    for i in range(0, len(array)):
        p = array[i]

        j = 0
        for j in range(i - 1, -1, -1):
            if array[j] > p:
                array[j + 1] = array[j]
            else:
                j += 1 # emulating C's composite for condition (; j>=0 && array[j]>p
                break

        array[j] = p

    return array
