class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # three different ways
        # 1.hash table Counter > 1 O(m+n)
        # 2. sorted + two pointers O(mlongm + nlogn)
        # 3. binary search on another list for every element O(mlongm + nlogm)
         
        # hash_table = {num: 0 for num in nums1}
        # for num in nums2:
        #     if num in hash_table:
        #         hash_table[num] += 1 
                
        # return [num for num, count in hash_table.items() if count > 0]
        
        # nums1, nums2 = sorted(nums1), sorted(nums2)
        # p1, p2 = 0, 0 
        # result = []
        # while p1 < len(nums1) and p2 < len(nums2):
        #     if nums1[p1] < nums2[p2]:
        #         p1 += 1 
        #     elif nums1[p1] > nums2[p2]:
        #         p2 += 1 
        #     else:
        #         if len(result) == 0 or result[-1] != nums1[p1]:
        #             result.append(nums1[p1])
        #         p1 += 1 
        #         p2 += 1 
                
        # return result 
        
        nums_loop, nums_search = (nums1, sorted(nums2)) if len(nums1) < len(nums2) else (nums2, sorted(nums1))
        result = set()
        for num in nums_loop:
            is_include = self.binary_search(num, nums_search)
            if is_include:
                result.add(num)
                
        return list(result)
        
    def binary_search(self, num, arrays):
        start, end = 0, len(arrays) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if arrays[mid] > num:
                end = mid 
            elif arrays[mid] < num:
                start = mid 
            else:
                return True 
                
        if arrays[start] == num or arrays[end] == num:
            return True 
        
        return False
