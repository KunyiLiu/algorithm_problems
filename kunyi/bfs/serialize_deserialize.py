"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        import Queue
        result = []
        if root is None:
            return ''
        queue = Queue.Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if node is None:
                result.append('#')
                continue
            result.append(node.val)
            queue.put(node.left)
            queue.put(node.right)
        
        # result = ''.join(result).rsplit('#', 1)[0]
        return result

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        import Queue
        if data == '':
            return None 
        
        data_list = data
        queue = Queue.Queue()
        root = TreeNode(data_list.pop(0))
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if len(data_list) > 0:
                left_val = data_list.pop(0)
                if left_val != '#':
                    left_node = TreeNode(left_val)
                    node.left = left_node
                    queue.put(left_node)
            if len(data_list) > 0:
                right_val = data_list.pop(0)
                if right_val != '#':
                    right_node = TreeNode(right_val)
                    node.right = right_node
                    queue.put(right_node)
                
        return root
