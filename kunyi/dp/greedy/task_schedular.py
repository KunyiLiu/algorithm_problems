######## heap #######
class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # count_dict = { char: count }
        # time: (n+1) * (nlogCat + Cat)
        from collections import Counter 
        import heapq
        counter_dict = Counter(tasks)
        result = 0
        while True:
            top_keys = [(-val, key) for key, val in counter_dict.items()]
            heapq.heapify(top_keys)
            if top_keys[0][0] == -1:
                result += len([_ for _, count in counter_dict.items() if count == 1])
                break
            else:
                result += (n+1)
            
            for i in range(n+1):
                if len(top_keys) == 0:
                    break
                tup = heapq.heappop(top_keys)
                if counter_dict[tup[1]] > 0:
                    counter_dict[tup[1]] -= 1 
                    
        return result

##### sorted #########
class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # count_dict = { char: count }
        # create_intervals: if (#key where count >= 1) > n, return (#key where count >= 1)
        # if (#key where count >= 1) <= n, return n + 1 
        # if (#key where count > 1) = 0 and (#key where count == 1), return (#key where count == 1)
        from collections import Counter 
        counter_dict = Counter(tasks)
        result = 0
        while True:
            top_keys = sorted(counter_dict.items(), key = lambda x: -x[1])
            if top_keys[0][1] == 1:
                result += len([_ for _, count in counter_dict.items() if count == 1])
                break
            else:
                result += (n+1)
            
            removed = 0    
            for key, count in top_keys:
                if count > 0:
                    counter_dict[key] -= 1
                    removed += 1 
                
                if removed == (n+1):
                    break
                    
        return result
        
###### math #######
## 最后所消耗的时间主要受制于出现次数最多的那个字母，所以我们可以推导出，所消耗的时间为 count(字母最多出现次数) * k - (其他字母贡献)

class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)
        # last level
        for count in counts:
            ans += count == longest and 1 or 0
            
        # "AAABCDEFGQWRT"  2
        # appending the remaining tasks
        return max(len(tasks), ans)
