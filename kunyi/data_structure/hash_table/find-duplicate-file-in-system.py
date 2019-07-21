class Solution:
    """
    @param paths: a list of string
    @return: all the groups of duplicate files in the file system in terms of their paths
    """
    def findDuplicate(self, paths):
        # hash_table[content] = [(directory, file) ...]
        hash_table = {}
        result = []
        for i, path in enumerate(paths):
            # python 3. root, *f = 'fdsfd dfsdf dsfsdf'.split(' ')
            path_list = path.strip().split(' ')
            directory = path_list[0]
            for file in path_list[1:]:
                file_list = file.rsplit('(')
                content = file_list[-1][:-1]
                if content not in hash_table:
                    hash_table[content] = []
                hash_table[content].append('/'.join([directory, file_list[0]]))
                
        
        for content, files in hash_table.items():
            if len(files) > 1:
                result.append(files)
                
        return result
