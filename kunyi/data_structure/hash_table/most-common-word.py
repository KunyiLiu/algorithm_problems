class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        # hash table, bucket sort 
        word_list, tmp = [], []
        for charac in paragraph:
            if charac.isalpha():
                tmp.append(charac)
            elif tmp:
                word_list.append(''.join(tmp))
                tmp = []
        if tmp:
            word_list.append(''.join(tmp))   
        word_counter = dict()
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in banned:
                word_counter[word_lower] = word_counter.get(word_lower, 0) + 1 
        
        max_count = max(word_counter.values())
        for word in word_counter:
            if word_counter[word] == max_count:
                return word
