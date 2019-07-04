class Solution:
    """
    @param s: a string
    @return: return List[str]
    """
    def findRepeatedDnaSequences(self, s):
        # hash_table['AAAAACCCCC'] = count
        n = len(s)
        result = []
        if n <= 10:
            return result
        hash_table, seq = {}, 'X' + s[:9]
        for i in range(9, n):
            # note that get slice = O(k)
            seq = seq[1:] + s[i]
            hash_table[seq] = hash_table.get(seq, 0) + 1
            
        for seq in hash_table:
            if hash_table[seq] >= 2:
                result.append(seq)
                
        return result
