class Solution:
    def shift_up(self, array, n, i):
        parent = (i - 1) // 2

        if parent >= 0:
            if array[i] > array[parent]:
                array[i], array[parent] = array[parent], array[i]

                self.shift_up(array, n, parent)
        return

    def insert_node(self, array, key):
        n = len(array) + 1
        # Insert the element at end of Heap
        # Heapify the new node following a Bottom-up approach
        array.append(key)
        self.shift_up(array, n, n - 1)


if __name__ == '__main__':
    array = [10, 5, 3, 2, 4]
    sol = Solution()
    sol.insert_node(array, 15)
    print(array)
