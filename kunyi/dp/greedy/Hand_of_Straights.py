### Sort O(nlogn) ####
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # greedy + stack -> car fleet
        # so there is left card after rearraingment?
        n = len(hand)
        if n % groupSize != 0:
            return False

        group_largest_array = [(None, 0)] * (n//groupSize)

        for h in sorted(hand):
            for i, group in enumerate(group_largest_array):
                if group[1] >= groupSize:
                    continue
                
                if group[0] is None or group[0] + 1 == h:
                    group_largest_array[i] = (h, group[1] + 1)
                    break

        for group in group_largest_array:
            if group[1] != groupSize:
                return False

        return True

        
