from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, words, k):
        counts, res = Counter(words), []
        freq = defaultdict(list)

        for word, count in counts.items():
            freq[count].append(word)
        max_freq = len(words)

        while max_freq >= 0:
            if max_freq in freq:
                res.extend(sorted(freq[max_freq]))
            max_freq -= 1
        return res[0:k]

'''
Submission Result: Accepted 
Next challenges: K Closest Points to Origin
110 / 110 test cases passed.
Status: Accepted
Runtime: 44 ms
Memory Usage: 13.1 MB

Related Topics: Hash Table, Heap, Trie
Similar Questions: Top K Frequent Elements, K Closest Points to Origin
'''
