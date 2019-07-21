class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # imitate the logic in 3Sum
        # O(n^3)
        length = len(numbers)
        numbers = sorted(numbers)
        result = []
        for i in range(length-3):
            if i and numbers[i] == numbers[i-1]:
                continue
            for j in range(i+1, length-2):
                if j > i + 1 and numbers[j] == numbers[j-1]:
                    continue
                tmp_result = []
                self.two_sum(numbers, j+1, length-1, target - numbers[i] - numbers[j], tmp_result)
                result.extend([[numbers[i], numbers[j], x[0], x[1]] for x in tmp_result])
                
        return result 
        
    def two_sum(self, array, start, end, target, result):
        while start < end:
            if array[start] + array[end] == target:
                result.append([array[start], array[end]])
                start += 1 
                end -= 1 
                while start < end and array[start] == array[start - 1]:
                    start += 1 
                while start < end and array[end] == array[end + 1]:
                    end -= 1 
            elif array[start] + array[end] > target:
                end -= 1 
            else:
                start += 1
