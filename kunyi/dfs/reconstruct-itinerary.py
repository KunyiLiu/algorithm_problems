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

### stack iteration ####
    def helper(self, hash_table, result, flight):
        stack = [flight]  # use stack with iteration to replace the recursion stack 
        while len(stack) > 0:
            latest_flight = stack[-1]
            if latest_flight in hash_table and hash_table[latest_flight]:
                to_flight = hash_table[latest_flight].pop(0)
                stack.append(to_flight)
            else:
                result.append(latest_flight)
                stack.pop()
### 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if tickets is None or len(tickets) == 0:
            return []
        
        tickets = sorted(tickets)  # in lexical order
        result = self.helper(tickets, ['JFK'])
        return result 
    
    def helper(self, tickets, result):
        if len(tickets) == 0:
            return result
        
        last_dest = result[-1]
        for i, (source, dest) in enumerate(tickets):
            if source == last_dest:
                result.append(dest)
                stack_result =  self.helper(tickets[:i] + tickets[(i+1):], result)
                ## Error 
                if stack_result: return stack_result
                result.pop()
                
        return
