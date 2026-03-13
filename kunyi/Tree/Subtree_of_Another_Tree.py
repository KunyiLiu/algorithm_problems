# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # pre-order: 1 2 4 5 3 substring
        # Time complexity: O(m + n)
        if root is None:
            return False

        root_serialized = self.serialize_preorder(root)
        subroot_serialized = self.serialize_preorder(subRoot)
        
        return subroot_serialized in root_serialized

    def serialize_preorder(self, root):
        if root is None:
            return '#'

        return ',' + str(root.val) + self.serialize_preorder(root.left) + self.serialize_preorder(root.right)


###  O(m * n) #

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # pre-order: 1 2 4 5 3
        # time complexity: O(m * n)
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        if self.isSubtree(root.left, subRoot):
            return True

        if self.isSubtree(root.right, subRoot):
            return True

        return False

    def isSameTree(self, root1, root2):
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            # always enque node at the same time
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
        
        return True

        
