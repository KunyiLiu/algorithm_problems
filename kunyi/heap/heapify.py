class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # Remember heap is a complete tree 
        # we should start from the lowest level heap (like the 1 as parent)
        
        for i in range((len(A) -1)/2, -1, -1):
            self.shiftdown(A, i)
            
    def shiftdown(self, A, ind):
        while ind * 2 + 1 < len(A):
            # select the smallest one
            son_ind = ind*2 + 1
            if son_ind + 1 < len(A) and A[son_ind + 1] < A[son_ind]:
                son_ind += 1 
                
            if A[son_ind] > A[ind]:
                break 
            
            A[son_ind], A[ind] = A[ind], A[son_ind]
            ind = son_ind

######### recursion ###########
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # get the parent of the last element 
        parent = (len(A) - 1) // 2 
        for i in range(parent, -1, -1):
            # heapify the subtree with root i 
            # bottom up 
            # O(n)
            self.heapify_root(A, i)
        
        return A
        
    def heapify_root(self, A, root):
        # top down
        smallest = root 
        left_child = 2*root + 1 
        right_child = 2*root + 2 
        if left_child < len(A) and A[left_child] < A[smallest]:
            smallest = left_child
        if right_child < len(A) and A[right_child] < A[smallest]:
            smallest = right_child
        
        if smallest != root:
            A[smallest], A[root] = A[root], A[smallest]
            self.heapify_root(A, smallest)
            
        return 
    
######## interation #########
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # get the parent of the last element 
        parent = (len(A) - 1) // 2 
        for i in range(parent, -1, -1):
            # heapify the subtree with root i 
            # bottom up 
            # O(n)
            self.heapify_root(A, i)
        
        return A
        
    def heapify_root(self, A, root):
        while root < len(A):
            smallest = root 
            left_child = 2*root + 1 
            right_child = 2*root + 2 
            if left_child < len(A) and A[left_child] < A[smallest]:
                smallest = left_child
            if right_child < len(A) and A[right_child] < A[smallest]:
                smallest = right_child

            if smallest != root:
                A[smallest], A[root] = A[root], A[smallest]
                root = smallest
            else:
                break
            
        return 
