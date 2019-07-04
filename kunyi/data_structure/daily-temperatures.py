######### stack ###########
class Solution:
    """
    @param temperatures: a list of daily temperatures
    @return: a list of how many days you would have to wait until a warmer temperature
    """
    def dailyTemperatures(self, temperatures):
        # min/max - stack 
        # the stack is to store index;
        # if [stack.peek] is less than [i], pop and res[stack.peek] = i - stack.peek
        # in the for loop, it is while loop to pop all of index, if [index] > [peek]
        # then we will push i into stack;
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)   
            
        return result
        
######### in reverse (decreasing order) #####
####### next[temperature] = ind #########
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            #Use 102 so min(nxt[t]) has a default value
            warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans
