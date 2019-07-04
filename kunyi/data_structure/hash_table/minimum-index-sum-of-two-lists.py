####### hash table ##########
class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """
    def findRestaurant(self, list1, list2):
        # hash_table[restaurant] = list of ind 
        # cornor case: tie
        from collections import defaultdict
        hash_table = defaultdict(list)
        result = []
        for ind, elem in enumerate(list1):
            hash_table[elem].append(ind)
        
        for ind, elem in enumerate(list2):
            hash_table[elem].append(ind)
        
        max_sum = min([sum(inds) for rest, inds in hash_table.items() if len(inds) >= 2]) 
        for rest, inds in hash_table.items():
            if len(inds) >= 2 and sum(inds) == max_sum:
                result.append(rest)
                
        return result
        
######### index ########
class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """

    def findRestaurant(self, list1, list2):
        # Write your code here
        ans = len(list1) + len(list2)
        s = []
        for andy in list1:
            if andy in list2:
                idx1 = list1.index(andy)
                idx2 = list2.index(andy)
                # first encounter, it is without doubt that sum(inds) would be the smallest
                if idx1 + idx2 < ans:
                    ans = idx1 + idx2
                    s = []
                    s.append(andy)
                elif idx1 + idx2 == ans:
                    s.append(andy)
        return s
