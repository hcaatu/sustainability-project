import sys
from codecarbon import track_emissions
from random import randint

# Helper function to merge two sorted portions of the list
def merge(arr, left, mid, right):
    
    n1 = mid - left + 1
    n2 = right - mid
    
    # Create temporary lists 
    # for left and right subarrays
    arr1 = arr[left:left + n1]
    arr2 = arr[mid + 1:mid + 1 + n2]
    
    i = 0    
    j = 0    
    k = left 
    
    # Merge the temp lists back into arr
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    
    # Copy remaining elements of arr1[] if any
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    
    # Copy remaining elements of arr2[] if any
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1

# Main sorting function
def mergeSort(arr):
    n = len(arr)
    
    # Iterate through subarrays of increasing size
    currSize = 1
    while currSize <= n - 1:
        
        # Pick starting points of different
        # subarrays of current size
        leftStart = 0
        while leftStart < n - 1:
            
            # Find endpoints of the subarrays to be merged
            mid = min(leftStart + currSize - 1, n - 1)
            rightEnd = min(leftStart + 2 * currSize - 1, n - 1)
            
            # Merge the subarrays arr[leftStart...mid]
            # and arr[mid+1...rightEnd]
            merge(arr, leftStart, mid, rightEnd)
            
            leftStart += 2 * currSize

        currSize = 2 * currSize

@track_emissions()
def main(argv):
    arr = []
    for i in range(int(argv)):
        arr.append(randint(1, 99999999))

    n = len(arr)
    print("Given array is length " + str(len(arr)))

    mergeSort(arr)
    print("Array sorted")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s array_size" % sys.argv[0])
    else:
        main(sys.argv[1])
