##### Time: O(n*n)
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
