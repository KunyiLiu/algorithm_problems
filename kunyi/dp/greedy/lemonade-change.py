class Solution:
    """
    @param bills: the Bill
    @return: Return true if and only if you can provide every customer with correct change.
    """
    def lemonadeChange(self, bills):
        # make the change 10 first (greedy)
        bills_count = { 5: 0, 10: 0 }
        for bill in bills:
            diff = bill - 5 
            if diff == 0:
                bills_count[5] += 1 
            elif diff == 5:
                bills_count[5] -= 1 
                bills_count[10] += 1 
            elif diff == 15:
                # first pay 10 
                if bills_count[10] > 0:
                    bills_count[10] -= 1 
                    bills_count[5] -= 1 
                else:
                    bills_count[5] -= 3
            
            if bills_count[5] < 0 or bills_count[10] < 0:
                return False 
                
        return True
