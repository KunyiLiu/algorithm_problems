class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def find(self, parent, x):
        if parent[x] == x:
            return x 
        
        parent[x] = self.find(parent, parent[x])
            
        return parent[x]
        
    def union(self, parent, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if x_root != y_root:
            parent[x_root] = parent[y_root]

        return 
        
    def accountsMerge(self, accounts):
        # time - O(#emails * # accounts) space - O(#emails)
        # # accounts - cost time of union and find operations
        from collections import defaultdict
        if accounts is None or len(accounts) == 0:
            return []
        
        email_id_table = dict()

        parent = list(range(len(accounts)))
        
        for ind, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_id_table:
                    email_id_table[email] = ind 
                self.union(parent, ind, email_id_table[email])
        
        for i in range(len(parent)):
            self.find(parent, i)
        
        result_table = defaultdict(set)
        for ind, root in enumerate(parent):
            result_table[root] |= set(accounts[ind][1:])
        
        return [[accounts[key][0]] + sorted(value_list) for key, value_list in result_table.items()]
