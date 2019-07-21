class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # insert house into heaters, find the heaters closest to the house 
        # min_radius = min(house - heaters_start, heaters_end - house)
        # get the global min_radius
        # Time: O(mlogn),  Space: O(1)
        heaters = sorted(heaters)
        min_radius = 0 
        for house in houses:
            heater_start_ind, heater_end_ind =  self.find_heaters(heaters, house)
            tmp_min_radius = min(abs(house - heaters[heater_start_ind]), abs(house - heaters[heater_end_ind]))
            min_radius = max(tmp_min_radius, min_radius)
            
        return min_radius
        
    def find_heaters(self, heaters, target):
        start, end = 0, len(heaters) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if heaters[mid] == target:
                return mid, mid 
            elif heaters[mid] > target:
                end = mid 
            else:
                start = mid 
        
        if heaters[start] == target:
            return start, start 
        if heaters[end] == target:
            return end, end 
        return start, end 
