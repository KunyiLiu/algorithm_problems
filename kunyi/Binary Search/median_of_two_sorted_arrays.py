###### O(log(m+n)) ######
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1, 2, 3, 4, 5] [3, 4, 5, 6]
        # [1, 2, 3, 3, 4, 4, 5, 5, 6] => 4 
        # given n + m elements, find the left partition, right partition ((n + m) // 2)
        # 1. first do binary search in a smaller array, the (n + m) // 2 - mid point is the BLeft
        # check if Aleft <= BRight && BLeft <= A Right
        # if not: then move the mid point of A to continue binary search
        # Return: if odd, min(Aright, Bright); if even, max(Aleft, Bleft) + min(Aright, Bright) / 2

        total = len(nums1) + len(nums2)
        A, B = nums1, nums2
        if len(A) >= len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            mid = l + (r - l) // 2
            j = total // 2 - mid - 2
            # mid could be < 0, A is too large, no A should be included
            # but mid could not be >= n, as Aright would be inf before this step,
            # basicall Aleft -> -inf, Aright ->inf same as Bleft, Bright
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            # left partition is now too large, decrease A portion
            elif Aleft > Bright:
                r = mid - 1
            else:
                # Bleft > Aright, incease A portion
                l = mid + 1


##### O(m + n) two pointers #######
# https://github.com/KunyiLiu/algorithm_problems/blob/e799b0044e45fd9f2386e16c192144bd85fda005/kunyi/data_structure_ii/median_of_two_sorted_arrays.py#L7


