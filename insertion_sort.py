import sys
from random import randint
from codecarbon import track_emissions

def insertionSort(arr):
    if len(arr) <= 1:
        return  # trivial case

    for i in range(1, len(arr)):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

@track_emissions
def main(argv):
    arr = []
    for i in range(int(argv)):
        arr.append(randint(1, 99999999))

    n = len(arr)
    print("Given array is length " + str(len(arr)))

    insertionSort(arr)
    print("Array sorted")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s array_size" % sys.argv[0])
    else:
        main(sys.argv[1])
