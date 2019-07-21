class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    hash_table = {}
    def add(self, number):
        # using hash table
        # can add duplicate
        if number not in self.hash_table:
            self.hash_table[number] = 0
        self.hash_table[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # hash_table[value - num] exists
        # O(n)
        for num in self.hash_table:
            if value - num != num and value - num in self.hash_table:
                return True 
            elif value - num in self.hash_table:
                return self.hash_table[value-num] > 1
                
        return False 
