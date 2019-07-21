import unittest
from collections import deque


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def last_level_first(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while len(q) > 0:
        q_length = len(q)
        for i in range(q_length):
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res[::-1]


class TestLastLevelFirst(unittest.TestCase):

    def test_root_is_none(self):
        self.assertEqual(last_level_first(None), [])

    def test_single_root(self):
        # set up
        root = TreeNode(3)
        # execute
        result = last_level_first(root)
        self.assertEqual(result, [3])

    def test_normal_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        result = last_level_first(root)
        self.assertEqual(result, [6, 5, 4, 3, 2, 1])

    def test_unbalanced_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        result = last_level_first(root)
        self.assertEqual(result, [3, 2, 1])

if __name__ == '__main__':
    unittest.main()
# This task requires values be printed out level by level starting from the bottom. The result is
# the same as storing the values level by level in a list starting from the root and then reversing the
# list. We use Breadth-first search to accomplish this since BFS explore all of the neighbors of a node
# before advancing to the next level. In this case, the neighbors are the left, right children of a node.
