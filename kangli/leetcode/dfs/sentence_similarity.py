class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        from collections import defaultdict
        if len(words1) != len(words2):
            return False
        sim_words = defaultdict(set)
        for p in pairs:
            sim_words[p[0]].add(p[1])
            sim_words[p[1]].add(p[0])
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words2[i] not in sim_words[words1[i]] or words1[i] not in sim_words[words2[i]]:
                    return False
            else:
                continue
        return True
