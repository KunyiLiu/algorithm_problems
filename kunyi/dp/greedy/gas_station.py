######   Greedy O(n) ######

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # find the first station that can reach the end of the array without the tank ever dipping below zero.
        # if A - B can pass, then at least there is some gas left, but to C failed, meaning it could not work either even starting from A - C.
        # so reset the first stop
        result = 0
        total_gas = 0

        for i in range(len(gas)):
            total_gas += (gas[i] - cost[i])
            if total_gas < 0:
                # reset
                total_gas = 0
                result = i + 1

        return result



################### TLE #####################
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if gas is None or cost is None or len(gas) == 0:
            return -1
        n = len(gas)
        possible_start_inds, max_gap = [], 0
        for i in range(n):
            if gas[i] >= cost[i] and (gas[i] - cost[i]) >= max_gap:
                possible_start_inds.append(i)
                max_gap = gas[i] - cost[i]
        
        # print(possible_start_inds)   
        for start in possible_start_inds:
            total_gas, end = 0, start 
            while True:
                total_gas = total_gas + gas[end] - cost[end]
                if total_gas >= 0:
                    end = (end + 1) % n  
                else:
                    break
                if end == start:
                    return start 
                    
        return -1
        
 ################# start from the last end ################
 class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if gas is None or cost is None or len(gas) == 0:
            return -1
        n = len(gas)
        diff = []
        for i in range(n):
            diff.append(gas[i]-cost[i])
        for i in range(n):
            diff.append(gas[i]-cost[i])
        
        # print(possible_start_inds)  
        start, end, total_gas = 0, 1, diff[0]
        while start < n:
            while total_gas < 0:
                # start from the last end 
                # why: if choose to start from the start + 1, total_gas -= diff[start], where diff[start] > 0
                # whill only smaller
                start = end 
                end += 1
                total_gas = diff[start]
                # already try one loop
                if start >= n:
                    return -1
            # end = start + 1
            while total_gas >= 0 and end != start + n:
                total_gas += diff[end]
                end += 1 
            if total_gas >= 0 and end == start + n:
                return start 
                    
        return -1
