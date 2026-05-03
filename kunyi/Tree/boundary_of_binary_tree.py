class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_boundary(root):
    # ask size and val
    if root is None:
        return []

    # 4 parts: root + left bounardy + leave + right boundary 
    result = [root]

    def is_leaf(node):
        if node is None:
            return False

        if node.left is None and node.right is None:
            return True

    # left bounardy
    cur_left = root.left
    while cur_left:
        if is_leaf(cur_left):
            break
        result.append(cur_left.val)
        cur_left = cur_left.left if cur_left.left else cur_left.right

    # leave nodes
    leaves = []
    def dfs(node):
        if node is None:
            return
        
        if is_leaf(node) and node != root: # Avoid adding root twice
            leaves.append(node.val)

        dfs(node.left)
        dfs(node.right)

        return

    dfs(root)
    result.extend(leaves)
    
    # right bounardy
    cur_right = root.right
    stack = []
    while cur_right:
        if is_leaf(cur_right):
            break
        stack.append(cur_right.val)
        cur_right = cur_right.right if cur_right.right else cur_right.left

    result.extend(stack[::-1])

    return result
