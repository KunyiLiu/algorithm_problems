########## Method 1  self.abs_diff = sys.maxsize . ##########
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # attention is not in uniqueness 
        # exit: abs_diff = 0 
        # tmp_sum > target, not necessary to move right 
        import sys
        numbers = sorted(numbers)
        self.diff = sys.maxsize
        for i in range(len(numbers)-2):
            self.two_sum(numbers, i+1, len(numbers) - 1, target - numbers[i])
            if self.diff == 0:
                return target
            
        return target + self.diff
        
    
    def two_sum(self, array, left, right, target):
        while left < right:
            tmp_sum = array[left] + array[right]
            if abs(tmp_sum - target) < abs(self.diff):
                self.diff = tmp_sum - target

            if tmp_sum > target :
                right -= 1 
            elif tmp_sum == target:
                return
            else:
                left += 1

###########  method 2 ################
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        numbers.sort()
        ans = None
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[right] + numbers[i]
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                    
                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return ans
