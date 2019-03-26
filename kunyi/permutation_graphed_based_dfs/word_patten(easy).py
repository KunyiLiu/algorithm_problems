class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        test_group = teststr.split(' ')
        if len(pattern) != len(test_group):
            return False 
            
        n = len(pattern)
        used, mapping = set(), {}
        for i in range(n):
            # chr in mapping, mapping(char) not consistent 
            # chr not in mapping but its correspoing word has been used
            if pattern[i] not in mapping:
                if test_group[i] in used:
                    return False 
                mapping[pattern[i]] = test_group[i]
                used.add(test_group[i])
            else: 
                if mapping[pattern[i]] != test_group[i]:
                    return False 
                    
        return True 
