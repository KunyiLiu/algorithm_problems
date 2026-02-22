class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Computes the bitwise AND of all numbers in the range [left, right].

        Key idea:
        - Any bit position where left and right differ will become 0 in the AND result,
          because that bit will flip at least once within the range.
        - Therefore, only the common prefix of left and right in binary contributes
          to the final result.

        Approach:
        - Shift left and right rightwards until they are equal, counting the number of shifts.
        - Shift the result back to reconstruct the AND of the range.

        Time Complexity: O(32) -> number of bits in the integer
        Space Complexity: O(1)
        """
        shift = 0

        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift
        
