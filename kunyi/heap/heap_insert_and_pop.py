class Solution:
    def shift_up(self, array, n, i):
        parent = (i - 1) // 2

        if parent >= 0:
            if array[i] > array[parent]:
                array[i], array[parent] = array[parent], array[i]

                self.shift_up(array, n, parent)
        return

    def shift_down(self, array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right

        if largest != i:
            array[largest], array[i] = array[i], array[largest]
            self.shift_down(array, n, largest)

        return

    def insert_node(self, array, key):
        n = len(array) + 1
        # Insert the element at end of Heap
        # Heapify the new node following a Bottom-up approach
        array.append(key)
        self.shift_up(array, n, n - 1)

    def pop_node(self, array):
        n = len(array)
        array[0], array[n - 1] = array[n - 1], array[0]
        self.shift_down(array, n - 1, 0)
        return array.pop()


if __name__ == '__main__':
    array = [10, 5, 3, 2, 4]
    sol = Solution()
    sol.insert_node(array, 15)
    print('insert 15', array)
    print('pop element {}, get heap {}'.format(sol.pop_node(array), array))
    print('pop element {}, get heap {}'.format(sol.pop_node(array), array))
    print('pop element {}, get heap {}'.format(sol.pop_node(array), array))
