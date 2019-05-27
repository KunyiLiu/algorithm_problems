#########  method 1: O(kn) ################
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # 1. counting sort {1: count1...k:countk}
        # 2, multiple partitions k times O(kn)
        
        if colors is None or len(colors) == 0:
            return []
        start, end = 0, len(colors) - 1
        for i in range(k):
            stored_ind = self.partition(colors, start, end, i+1)
            start = stored_ind
            
        return colors
    
    def partition(self, colors, start, end, target):
        while start <= end:
            while start <= end and colors[start] == target:
                start += 1 
            while start <= end and colors[end] != target:
                end -= 1 
                
            if start <= end:
                colors[start], colors[end] = colors[end], colors[start]
                start += 1 
                end -= 1 
                
        return start 
        
 ######### method 2: D&Q, T(k) = 2T(k/2) + O(n) = O(nlogk) ###########
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors) - 1)
        
    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return
            
        color = (color_from + color_to) // 2
        
        left, right = index_from, index_to
        while left <= right:
            # all left elems <= target color
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        
        self.sort(colors, color_from, color, index_from, right)
        self.sort(colors, color + 1, color_to, left, index_to)

        
 ##### rainbow sort - counting sort ######
## 在数字范围较小的时候效率高，空间复杂度是数字的范围。是说统计每个数字出现的次数，然后从小到大排序
