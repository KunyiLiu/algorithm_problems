######## BFS O(N) ######

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        
        queue = [(target, 0)]
        seen = set([target])
        while queue:
            # queue's first element -first input
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, dist = queue.pop(0)
            for nei in [node.left, node.right, node.par]:
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist+1))

        return []
        
        
 ####   DFS   #########
 """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    """
    def distanceK(self, root, target, K):
        # Write your code here
        # top down: target node, find its nodes with k ditance in the downwards direction
        # bottom up: find from root, if target, return 0, find until dis == K;
        #            if dis < k, run top_down_search(root, dis - k)
        self.result_list = []
        self.top_down_search(target, K, 0)
        self.bottom_up_search(root, target, K)
            
        return self.result_list
        
    def top_down_search(self, target, K, current_dis):
        if current_dis == K:
            self.result_list.append(target.val)
            return 
        
        if target is None:
            return 
        
        if target.left:
            self.top_down_search(target.left, K, current_dis + 1)
        
        if target.right:
            self.top_down_search(target.right, K, current_dis + 1)
            
        return 
    
    def bottom_up_search(self, node, target, K):
        if node == target:
            return 0
            
        if node is None:
            return node
            
        left_dis = self.bottom_up_search(node.left, target, K)
        if left_dis is not None:
            if left_dis + 1 == K:
                self.result_list.append(node.val)
            elif left_dis + 1 < K:
                self.top_down_search(node.right, K - left_dis - 2, 0)
            return left_dis + 1
        right_dis = self.bottom_up_search(node.right, target, K)
        if right_dis is not None:
            if right_dis + 1 == K:
                self.result_list.append(node.val)
            elif right_dis + 1 < K:
                self.top_down_search(node.left, K - right_dis - 2, 0)
            return right_dis + 1
            
        return
        
