class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # assume all the people choose A, so that sum = sum(costs[i][0])
        # then we need to pick n people to choose B. Each persion choice to the sum, diff = costs[i][1] - costs[i][0]
        # so we sort them, and pick the smallest n numbers 
        n = len(costs) // 2
        costs = sorted(costs, key=lambda x: x[1] - x[0])
        result_sum = sum([_[0] for _ in costs])
        result_sum += sum([(_[1] - _[0]) for _ in costs[:n]])
        return result_sum
        
