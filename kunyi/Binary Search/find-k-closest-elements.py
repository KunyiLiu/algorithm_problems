############################ find critical point closest to 0  #############
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # find the two critical points closest to 0 
        # ideally would be diff < 0 and diff > 0 respectively
        # then start from these two points, get k points (two pointers)
        if A is None or len(A) == 0 or k == 0:
            return []
            
        result = []
        start, end = 0, len(A) - 1
        critical_point = -1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] - target > 0:
                end = mid 
            elif A[mid] - target < 0:
                start = mid 
            else:
                critical_point = mid
                break
        else:
            # ERROR 1. what if A[start] and A[end] have same val
            # if diff equals, choose start
            critical_point = start if self.abs_diff(A[start],target) <= self.abs_diff(A[end], target) else end

        result.append(A[critical_point])
        left, right = critical_point - 1, critical_point + 1 
        while left >= 0 and right < len(A):
            if len(result) == k:
                break
            if self.abs_diff(A[left], target) <= self.abs_diff(A[right], target):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        
        # ERROR2.len not enough
        while len(result) < k and right < len(A):
            result.append(A[right])
            right += 1 
            
        while len(result) < k and left >= 0:
            result.append(A[left])
            left -= 1
                
        return result 
            
    def abs_diff(self, num, target):
        return abs(num - target)
        
############################    find the first number >= target in A ###################
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # 找到 A[left] < target, A[right] >= target
        # 也就是最接近 target 的两个数，他们肯定是相邻的
        right = self.find_upper_closest(A, target)
        left = right - 1
    
        # 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        
        return results
    
    def find_upper_closest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        
        if A[start] >= target:
            return start
        
        if A[end] >= target:            
            return end
        
        # 找不到的情况
        return end + 1
        
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
