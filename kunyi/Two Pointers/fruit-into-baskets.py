############### let next start be the smallest index of valid array [i,j] ####################
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # choose the ind where tree[i], treee[j] most frequent
        # first - first bucket
        # second - second bucket 
        # if first > second and first number is 3rth number 
        # first, second = second + 1, first
        longest = 0 
        n = len(tree)
        if n >= 1:
            count = dict()
        else:
            return longest
        ind, tmp = 0, 0
        while ind < n:
            if tree[ind] in count:
                count[tree[ind]] = ind 
                tmp += 1
            elif len(count.keys()) <= 1:
                count[tree[ind]] = ind
                tmp += 1
            else:
                longest = max(longest, tmp)
                first = sorted([(key, val) for key, val in count.items()], key=lambda x: x[1])[0]
                del count[first[0]]
                ind = first[1]
                # error
                tmp = 0
            ind += 1
        longest = max(longest, tmp)
        return longest
        
####################### remove the count to remain len(count) ==2 ####################
"""
Let's perform a sliding window, keeping the loop invariant that i will be the smallest index for which [i, j] is a valid subarray.

We'll maintain count, the count of all the elements in the subarray. This allows us to quickly query whether there are 3 types in the subarray or not.
"""
class Solution(object):
    def totalFruit(self, tree):
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
