class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                cur_string = ""
                num = ""
                while stack:
                    temp = stack.pop()
                    if temp == '[':
                        break
                    cur_string = temp + cur_string
                while stack:
                    if stack[-1].isdigit():
                        num = stack.pop() + num
                    else:
                        break
                cur_string = int(num)*cur_string 
                stack.append(cur_string)
            else:
                stack.append(c)
        return "".join(stack)
        
        
'''
Success
Details 
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Decode String.
Memory Usage: 13.9 MB, less than 5.68% of Python3 online submissions for Decode String.
Next challenges: Encode String with Shortest Length, Number of Atoms, Brace Expansion
'''
