"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # pivot - nut 
        # loop through nuts, stored_ind change as i change
        # O(n^2)
        n = len(nuts)
        for i, nut in enumerate(nuts):
            for j in range(i, n):
                if compare.cmp(nut, bolts[j]) == 0:
                    break 
                
            bolts[i], bolts[j] = bolts[j], bolts[i]
