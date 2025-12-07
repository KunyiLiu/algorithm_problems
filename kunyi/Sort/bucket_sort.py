"""
Bucket Sort is a sorting algorithm that:

1. Divides input elements into multiple buckets (groups) based on their value range.

2. Sorts each bucket individually (often using another algorithm like insertion sort or quicksort).

3. Concatenates all buckets to get the final sorted output.

When it's useful

Works best when:

1. values are uniformly distributed

2. you know the value range in advance

3. suitable for floating numbers or bounded integers
"""

# for floating values (0, 1)
def bucket_sort_float(arr):
    n = len(arr)
    if n == 0:
        return arr

    # Step 1: Create N empty buckets
    buckets = [[] for _ in range(n)]

    # Step 2: Assign elements to buckets
    for num in arr:
        index = int(num * n)     # maps value to bucket index
        buckets[index].append(num)

    # Step 3: Sort each bucket (using Python built-in sort or insertion sort)
    for i in range(n):
        buckets[i].sort()        # typical implementation uses insertion sort

    # Step 4: Merge buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


# Example
arr = [0.21, 0.73, 0.13, 0.52, 0.41, 0.93, 0.27]
print(bucket_sort_float(arr))

# for intergers with known range

def bucket_sort_int(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    # Step 1: Find range
    min_val, max_val = min(arr), max(arr)

    # Step 2: Create buckets
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Step 3: Distribute numbers
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # Step 4: Sort each bucket and merge
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result


# Example
arr = [42, 32, 33, 52, 37, 47, 51]
print(bucket_sort_int(arr, bucket_size=5))



