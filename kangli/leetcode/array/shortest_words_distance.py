class Solution(object):
    def shortestDistance(self, words, word1, word2):
        dist = len(words)
        pos0, pos1 = [], []
        for i, w in enumerate(words):
            if w == word1:
                pos0.append(i)
            elif w == word2:
                pos1.append(i)
        for p1 in pos0:
            for p2 in pos1:
                dist = min(dist, abs(p2 - p1))
        return dist
