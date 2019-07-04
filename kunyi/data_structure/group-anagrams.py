class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # SET 1
        # pseudocode
        # first set up a hash table for character count for each string within the given list
        # if the current character count in the tmp list of dict, 
        # get the index and append to the corresponeding sublist within the result list
        # else
        # append character count to the list and create a new sublist
        ## character_counts  [{'a':1, 'e': 1, 't': 1}, {...], ...]
        # TIme complexisity: 
        # traverse through the whole list - 0{nm}, each word has maximum M characters
        result = []
        if len(strs) == 0:
            return result
        character_counts = []
        for substr in strs:
            tmp = {}
            for i in substr:
                if i not in tmp:
                    tmp[i] = 1 
                else:
                    tmp[i] += 1 
            if tmp in character_counts:
                ind = character_counts.index(tmp)
                result[ind].append(substr)
            else:
                character_counts.append(tmp)
                result.append([substr])
        return result
        
        # set 2
        # get sorted version of each words in strs list, like ['aet', 'aet', ...]
        # make it the key as the dic {'aet': ['eat', ..], ..}
        from collections import defaultdict
        word_hash = defaultdict(list)
        for substr in strs:
            hash = ''.join(sorted(substr))
            word_hash[hash].append(substr)
            
        result = [v for k,v in word_hash.items()]
        return result
