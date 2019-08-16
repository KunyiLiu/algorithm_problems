class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # time/space: O(n)
        mod_time = map(lambda x: x % 60, time)
        time_ind_dict = dict()
        count = 0 
        for ind, item in enumerate(mod_time):
            if 60 - item in time_ind_dict:
                count += time_ind_dict[60 - item]
            elif item in time_ind_dict and item == 0:
                count += time_ind_dict[item]
            time_ind_dict[item] = time_ind_dict.get(item, 0) + 1 
            
        return count 
