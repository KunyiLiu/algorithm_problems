class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        roots = list(range(len(accounts)))
        
        def find_root(account_id):
            if roots[account_id] == account_id:
                return account_id
            roots[account_id] = find_root(roots[account_id])
            return roots[account_id]
        
        def union(a, b):
            roots[find_root(b)] = find_root(a)
        
        email_to_id = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email] = i 
        id_email = defaultdict(set)
        
        for account in accounts:
            for email in account[1:]:
                root_id = find_root(email_to_id[email])
                name = accounts[root_id][0]
                id_email[(root_id, name)].add(email)
            
        res = []
        for k, v in id_email.items():
            emails = sorted(v)
            name = k[1]
            res.append([name]+emails)
        return res


'''
Success
Details 
Runtime: 240 ms, faster than 70.90% of Python3 online submissions for Accounts Merge.
Memory Usage: 17.5 MB, less than 58.82% of Python3 online submissions for Accounts Merge.
Next challenges: Sentence Similarity, Sentence Similarity II
'''
