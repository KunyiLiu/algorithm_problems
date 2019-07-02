class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def isPossible(self, nums):
        # write your code here
        counter, tails = {}, {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1 
            
        for num in nums:
            if counter[num] == 0: continue
            # append to the existing array with tail num == num-1
            if num-1 in tails and tails[num-1] > 0:
                tails[num-1] -= 1 
                tails[num] = tails[num] + 1 if num in tails else 1 
            elif counter.get(num+1, 0) and counter.get(num+2, 0):
                counter[num+1] -= 1 
                counter[num+2] -= 1
                tails[num+2] = tails[num+2] + 1 if num+2 in tails else 1
            else:
                return False 
            counter[num] -= 1 
            
        return True
