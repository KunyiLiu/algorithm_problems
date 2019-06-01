# elements in array must be sorted first
# return any ind that equal to target
# time comlexity is O(log3N), but is worse than binary search in the worse cases

def ternary_search(array, target, left, right):
    start, end = left, right
    if start + 1 < end:
        mid_1 = start + (end - start) // 3
        mid_2 = end - (end - start) // 3
        if array[mid_1] == target:
            return mid_1
        if array[mid_2] == target:
            return mid_2
        if array[mid_2] < target:
            return ternary_search(array, target, mid_2 + 1, right)
        if array[mid_1] > target:
            return ternary_search(array, target, left, mid_1 - 1)

        return ternary_search(array, target, mid_1 + 1, mid_2 - 1)

    if array[start] == target:
        return start
    if array[end] == target:
        return end


if __name__ == '__main__':
    array = [1, 5, 7, 8, 13, 45, 124, 234]
    target = 124
    print('The result index of target {} is {}'.format(target, ternary_search(array, target, 0, len(array) - 1)))
