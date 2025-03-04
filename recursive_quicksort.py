import sys
from codecarbon import track_emissions
from random import randint

def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


@track_emissions()
def main(argv):
    arr = []
    for i in range(int(argv)):
        arr.append(randint(1, 99999999))

    n = len(arr)
    print("Given array is length " + str(len(arr)))

    quickSort(arr, 0, n - 1)
    print("Array sorted")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s array_size" % sys.argv[0])
    else:
        main(sys.argv[1])
        