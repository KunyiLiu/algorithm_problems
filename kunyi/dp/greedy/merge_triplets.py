class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target

        attempt = [-1, -1, -1]

        for triplet in triplets:
            # condition: if there is at least one elem == target's elem, and no
            # elem > target's elem, then override the attempt with the current triplet
            for i in range(3):
                if triplet[i] > target[i]:
                    break
            else:
                for i in range(3):
                    attempt[i] = max(attempt[i], triplet[i])

        return attempt == target


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for t in triplets:
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
            if x and y and z:
                return True
        return False
