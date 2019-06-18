class Solution:
    """
    @param tickets: 
    @return: nothing
    """
    def findItinerary(self, tickets):
        # Write your code here
        hash_table = {}
        for ticket in tickets:
            if ticket[0] not in hash_table:
                hash_table[ticket[0]] = []
            hash_table[ticket[0]].append(ticket[1])
            
        # sort the hash_table, reverse
        for key in hash_table:
            hash_table[key] = sorted(hash_table[key])[::-1]
        
        # 将从一个机场可以到达的所有机场逆序排序，再DFS找出答案
        result = []
        self.helper(hash_table, result, 'JFK')
        return result[::-1]
        
    def helper(self, hash_table, result, flight):
        while flight in hash_table and hash_table[flight]:
            to_flight = hash_table[flight].pop()
            self.helper(hash_table, result, to_flight)
        result.append(flight)
            
        return 
