import sys
from random import shuffle, randint
from codecarbon import track_emissions

def bogoSort(arr):
    print('unsorted array')
    print(arr)
    # trivial case
    if len(arr) <= 1:
        return arr
    
    while sorted(arr) == False:
        shuffle(arr)
    print('sorted array')
    print(arr)
    return arr
    
def sorted(arr):
    for index in range(0, len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return False
    return True
        

@track_emissions
def main(argv):
    arr = []
    for i in range(int(argv)):
        arr.append(randint(1, 99999999))

    n = len(arr)
    print("Given array is length " + str(len(arr)))

    bogoSort(arr)
    print("Array sorted")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s array_size" % sys.argv[0])
    else:
        main(sys.argv[1])
