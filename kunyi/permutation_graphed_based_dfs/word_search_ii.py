##### Trie + Backtrack - Time complexity: O(m * n * 3 ^L)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_final = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        head = self.root
        for w in word:
            if w not in head.children:
                head.children[w] = TrieNode()

            head = head.children[w]

        head.is_final = True

    def buildTrie(self, words):
        for word in words:
            self.addWord(word)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make the workds a Trie, then find the word in board
        # Time complexity: O(m * n * 3^L), L the max length of words
        # 4 directions, But you cannot revisit cells → effectively branching ~3 after first step
        trie = Trie()
        trie.buildTrie(words)
        trie_root = trie.root

        m, n = len(board), len(board[0])
        # use result hashset to prevent finding duplicate words
        result = set()

        def dfs(x, y, trie_node, subset, visited):
            if trie_node.is_final:
                result.add(''.join(subset))
                # not return here, otherwise only "back" and not "backend" included

            delta_X = [1,-1,0, 0]
            delta_Y = [0,0,1,-1]
            for i in range(4):
                new_x = delta_X[i] + x
                new_y = delta_Y[i] + y
                if 0 <= new_x < m and 0 <= new_y < n and (board[new_x][new_y] in trie_node.children) and (new_x, new_y) not in visited:
                    subset.append(board[new_x][new_y])
                    visited.add((new_x, new_y))
                    dfs(new_x, new_y, trie_node.children[board[new_x][new_y]], subset, visited)
                    subset.pop()
                    visited.remove((new_x, new_y))

            return

        for i in range(m):
            for j in range(n):
                chr = board[i][j] 
                if chr in trie_root.children:
                    dfs(i, j, trie_root.children[chr], [chr], set([(i,j)]))

        return list(result)

#####  Backtrack - Time Complexity: O(w * m * n * 3 ^ L)
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if len(board) == 0 or len(board[0]) == 0:
            return []
        self.m, self.n = len(board), len(board[0])
        self.deltaX = [-1, 0, 1, 0]
        self.deltaY = [0, -1, 0, 1]
        result = []
        for word in words:
            inds = self.get_first_position(word, board)
            if len(inds) == 0:
                continue
            for ind in inds:
                matched = self.helper(word[1:], board, [ind])
                if matched:
                    result.append(word)
                    break

        return result 
        
    def get_first_position(self, word, board):
        first_inds = []
        for i in range(self.m):
            for j in range(self.n):
                if word[0] == board[i][j]:
                    first_inds.append((i,j))
                    
        return first_inds
        
    def helper(self, word, board, last_inds):
        if len(word) == 0:
            return True 
        
        first_char = word[0]
        last_ind = last_inds[-1]
        x, y = last_ind[0], last_ind[1]
        for i in range(4):
            new_x, new_y = x + self.deltaX[i], y + self.deltaY[i]
            if 0 <= new_x < self.m and 0 <= new_y < self.n and first_char == board[new_x][new_y] and (new_x, new_y) not in last_inds:
                if self.helper(word[1:], board, last_inds + [(new_x, new_y)]):
                    return True 
                # do not return False yet, go to check another pair of (new_x, new_y)
                
        return False
