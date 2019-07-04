######## hash table #######
class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # x in list O(n); x in dict O(1) in average case 
        from collections import Counter
        count = Counter(J)
        result = 0 
        for char in S:
            if char in count:
                result += 1 
                
        return result


###### hash set #######
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # 利用set即可。
        return sum([ch in set(J) for ch in S])
