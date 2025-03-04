import sys
from random import randint
from codecarbon import track_emissions

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

@track_emissions
def main(argv):
    arr = []
    for i in range(int(argv)):
        arr.append(randint(1, 99999999))

    n = len(arr)
    print("Given array is length " + str(len(arr)))

    bubbleSort(arr)
    print("Array sorted")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s array_size" % sys.argv[0])
    else:
        main(sys.argv[1])
