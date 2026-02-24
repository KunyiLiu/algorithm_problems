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

###### greedy O(n)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # greedy + stack -> car fleet
        # so there is left card after rearraingment?
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            if count[num] == 0: continue # Skip if we already used this card

            start = num
            # find the smallest card, set it as start
            while count[start - 1]:
                start -= 1
            while count[start]:
                for i in range(start, start + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1

        return True
        
