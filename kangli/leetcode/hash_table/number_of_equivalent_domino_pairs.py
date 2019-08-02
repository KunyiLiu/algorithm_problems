class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = {}
        for domino in dominoes:
            (a, b) = sorted(domino)
            pairs[(a, b)] = pairs.get((a, b), 0)+1
        count = 0 
        for v in pairs.values():
            count += v*(v-1)//2
        return count


'''
Success
Details 
Runtime: 284 ms, faster than 41.19% of Python3 online submissions for Number of Equivalent Domino Pairs.
Memory Usage: 23.6 MB, less than 100.00% of Python3 online submissions for Number of Equivalent Domino Pairs.
Next challenges: Spiral Matrix, Product of Array Except Self, Third Maximum Number

Related Topics: Array
Hints: 1) For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.
2) You can keep track of what you've seen using a hashmap.
'''
