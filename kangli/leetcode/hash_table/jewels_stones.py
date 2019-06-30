class Solution:
    def numJewelsInStones(self, J, S):
        j_list = list(J)
        count = 0
        for stone in S:
            if stone in j_list:
                count += 1
        return count

'''
Success
Details
Runtime: 36 ms, faster than 80.97% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.1 MB, less than 77.65% of Python3 online submissions for Jewels and Stones.
Next challenges:
Bulls and Cows
Minimum Area Rectangle
Vowel Spellchecker

Related Topics: Hash Table
Hint: For each stone, check if it is a jewel. 
'''
