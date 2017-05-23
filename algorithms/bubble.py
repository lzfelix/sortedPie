def sort(array):

    n = len(array)

    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

    return array

if __name__ == '__main__':
    r = range(100)
    sort(r)