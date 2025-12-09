class MaxHeap:
    def __init__(self):
        self.heap = []

    # ---------------------------
    # BUILD HEAP (O(N))
    # ---------------------------
    def heapify(self, array):
        self.heap = array
        n = len(self.heap)

        # start from last parent to the first parent, 
        # ensure the deeper subtree is max-heap
        for parent in range((n - 1) // 2, -1, -1):
            self._shiftdown(n, parent)

    # ---------------------------
    # PUSH (O(log N))
    # ---------------------------
    def heappush(self, key):
        self.heap.append(key)                 # put at end
        self._shiftup(len(self.heap) - 1)     # bubble up

    # ---------------------------
    # POP MAX (O(log N))
    # ---------------------------
    def heappop(self):
        if not self.heap:
            return None
        
        n = len(self.heap)
        # swap root (max) with last element
        self.heap[0], self.heap[n - 1] = self.heap[n - 1], self.heap[0]
        
        max_value = self.heap.pop()           # remove last (max)
        self._shiftdown(len(self.heap), 0)     # restore heap
        return max_value

    # ---------------------------
    # INTERNAL: SHIFT DOWN
    # ---------------------------
    def _shiftdown(self, end, parent):
        heap = self.heap

        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2
            largest = parent

            if left < end and heap[left] > heap[largest]:
                largest = left
            if right < end and heap[right] > heap[largest]:
                largest = right

            if largest == parent:
                break

            heap[parent], heap[largest] = heap[largest], heap[parent]
            parent = largest

    # ---------------------------
    # INTERNAL: SHIFT UP
    # ---------------------------
    def _shiftup(self, index):
        heap = self.heap

        while index > 0:
            parent = (index - 1) // 2
            if heap[index] <= heap[parent]:
                break
            
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
