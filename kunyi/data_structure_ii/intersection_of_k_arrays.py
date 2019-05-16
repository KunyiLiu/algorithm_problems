##############################   heap/priority queue ###############################
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # 基于 Priority Queue 的版本。
        # 假设每个数组长度为 n, 一共 k 个数组。
        # 时间复杂度为 O(knlogn + nklogk)O(knlogn+nklogk)
        # 其中 knlognknlogn 是 k 个数组进行分别排序的时间复杂度
        # nklogknklogk 是 总共 nk 个数从 PriorityQueue 中进出，每次进出 logk
        import heapq
        heap = []
        intersection_count, array_count = 0, 0 
        last_val = None
        for i in range(len(arrs)):
            arrs[i] = sorted(arrs[i])
            if len(arrs[i]) > 0:
                heapq.heappush(heap, (arrs[i][0], i, 0))
                
        while len(heap) > 0:
            elem, row, ind = heapq.heappop(heap)
            if elem != last_val or array_count == 0:
                array_count = 1 
                last_val = elem
            else:
                array_count += 1 
                
            if array_count == len(arrs):
                intersection_count += 1 
                
            if ind + 1 < len(arrs[row]):
                heapq.heappush(heap, (arrs[row][ind+1], row, ind + 1 ))
                
        return intersection_count
        
#########################        set #################################
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # kO(n)
        while len(arrs) > 1:
            new_set = self.intersect_two_arrays(arrs[-1], arrs[-2])
            del arrs[-1]
            del arrs[-1]
            arrs.append(new_set)
            
        return len(arrs[0])
        
    def intersect_two_arrays(self, arr1, arr2):
        return list(set(arr1) & set(arr2))
        
 ##################   hash map #################################
 class Solution:
    def intersectionOfArrays(self, arrs):
        M = {}
        for i in arrs:
            for j in i:
                if j in M:
                    M[j] = M[j] + 1
                else:
                    M[j] = 1
        ans = 0
        for k,v in M.iteritems(): 
            if v == len(arrs):
                ans += 1
        return ans
