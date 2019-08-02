class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.split('.')
        return '[.]'.join(address)
            

'''
Success
Details 
Runtime: 36 ms, faster than 63.18% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
Next challenges: Valid Palindrome, Remove Vowels from a String, Parsing A Boolean Expression
'''
