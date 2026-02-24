#####  Stack ######
class Solution:
    def checkValidString(self, s: str) -> bool:
        # order matters -> 1. DFS + memo O(n**n)
        # 2. stack O(n), 3. greedy
        left = []
        star = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if len(left) == 0 and len(star) == 0:
                    return False

                if left:
                    left.pop()

                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False

        # if there is any left remainning
        return not left

#### Greedy ####
class Solution:
    def checkValidString(self, s: str) -> bool:
        # order matters -> 1. DFS + memo O(n**n)
        # 2. stack O(n) for Time and space, 3. greedy: Time O(n), Space O(1)
        # left Min/Max - the min/Max boundary of the ummatech (;
        # if ) -> leftMin - 1, leftMax - 1;
        # if * -> leftMin - 1 (if * -> ')'), leftMax + 1 (if * -> '(')
        leftMin, leftMax = 0, 0

        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                # too much )
                # it means even if you treated every single * as an opening bracket (, 
                # you still have too many closing brackets )
                return False

            # Reset leftMin: we can't have fewer than 0 open parentheses
            if leftMin < 0:
                leftMin = 0

        # At the end, we must be able to reach exactly 0 open parentheses
        return leftMin == 0
        
