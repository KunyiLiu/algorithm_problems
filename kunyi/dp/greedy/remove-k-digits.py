####### if break #####
class Solution:
    """
    @param num: a string
    @param k: an integer
    @return: return a string
    """
    def removeKdigits(self, num, k):
        # remove K: 1. high-order digit 2. larger digit 
        # if encouter 0, pop out the top (remove two digits implicitly)
        # O(n)
        # 可以使用单调栈。
        # 从高位向低位依次入栈，若当前数字小于栈顶元素且k不为0，则删除栈顶元素。
        # 最后将栈内的元素变为数字即可。
        stack = []
        if len(num) == k:
            return '0'
        for ind, char in enumerate(num):
            while len(stack) > 0 and k > 0 and char < stack[-1]:
                stack.pop()
                k -= 1 
            # when char == '0' and remove all the preceding nums in stack 
            # not append to stack
            stack.append(char)
            if k == 0:
                break
        else:
            while k > 0 and len(stack) > 0:
                stack.pop()
                k -= 1 
            
        return (''.join(stack) + num[ind+1:]).lstrip('0')
        
        
######### Method 2 #######
    def removeKdigits(self, num, k):
        # remove K: 1. high-order digit 2. larger digit 
        # if encouter 0, pop out the top (remove two digits implicitly)
        # O(n)
        stack = []
        if len(num) == k:
            return '0'
        for ind, char in enumerate(num):
            while len(stack) > 0 and k > 0 and char < stack[-1]:
                stack.pop()
                k -= 1 
            # when char == '0' and remove all the preceding nums in stack 
            # not append to stack
            if char != '0' or len(stack) > 0:
                stack.append(char)

        while k > 0 and len(stack) > 0:
            stack.pop()
            k -= 1 
            
        return ''.join(stack)
