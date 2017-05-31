def sort(array, step_size=1):
    for i in range(0, len(array), step_size):
        p = array[i]

        j = 0
        for j in range(i - step_size, -1, -step_size):
            if array[j] > p:
                array[j + step_size] = array[j]
            else:
                j += step_size  # emulating C's composite for condition (; j>=0 && array[j]>p
                break

        array[j] = p

    return array
