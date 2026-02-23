class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # create two monotonic stacks - ensure the stacks increasing, 
        # stack A - find the next index with smaller value;
        # stack B - reverse iterate, find the previous index with smaller value
        # time: O(n), space: O(n)
        n = len(heights)
        # if not found
        next_smaller_ind = [n] * n
        pre_smaller_ind = [-1] * n

        next_smaller_stack = []
        pre_smaller_stack = []

        for i, h in enumerate(heights):
            while next_smaller_stack and h < heights[next_smaller_stack[-1]]:
                ind = next_smaller_stack.pop()
                next_smaller_ind[ind] = i

            next_smaller_stack.append(i)

        for i in range(n - 1, -1, -1):
            h = heights[i]
            while pre_smaller_stack and h < heights[pre_smaller_stack[-1]]:
                ind = pre_smaller_stack.pop()
                pre_smaller_ind[ind] = i

            pre_smaller_stack.append(i)

        max_area = 0
        for i in range(n):
            diff = next_smaller_ind[i] - pre_smaller_ind[i] - 1
            area = diff * heights[i]
            max_area = max(max_area, area)

        return max_area




        
