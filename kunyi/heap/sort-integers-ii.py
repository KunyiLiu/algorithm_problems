####### deletion #######
    // Function to delete the root from Heap 
    static int deleteRoot(int arr[], int n) 
    { 
        // Get the last element 
        int lastElement = arr[n - 1]; 
  
        // Replace root with first element 
        arr[0] = lastElement; 
  
        // Decrease size of heap by 1 
        n = n - 1; 
  
        // heapify the root node 
        heapify(arr, n, 0); 
  
        // return new size of Heap 
        return n; 
    } 

### insert 
// Function to insert a new node to the Heap 
void insertNode(int arr[], int& n, int Key) 
{ 
    // Increase the size of Heap by 1 
    n = n + 1; 
  
    // Insert the element at end of Heap 
    arr[n - 1] = Key; 
  
    // Heapify the new node following a 
    // Bottom-up approach 
    heapify(arr, n, n - 1); 
} 

##### sort
    
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # quick sort 
        # O(nlogn)
        if len(A) == 0:
            return A
        parent = (len(A) - 1) // 2 
        for i in range(parent, -1, -1):
            self.heapify(A, len(A), i)
        
        # first determine the last element of A (max)
        # reverse last element and first (max)
        for i in range(len(A) - 1 , 0, -1):
            A[i], A[0] = A[0], A[i]
            self.heapify(A, i, 0)
            
        return A
        
    def heapify(self, A, n, root):
        largest = root
        left_child = 2 * root + 1 
        right_child = 2 * root + 2 
        if left_child < n and A[left_child] > A[largest]:
            largest = left_child
        if right_child < n and A[right_child] > A[largest]:
            largest = right_child
        
        if largest != root:
            A[largest], A[root] = A[root], A[largest]
            self.heapify(A, n, largest)
            
