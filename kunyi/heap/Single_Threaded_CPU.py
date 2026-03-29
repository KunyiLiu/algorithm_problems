# waiting priority queue 
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # first sort the tasks based on starttime, costtime, ind.
        # minheap represents the tasks ready to be processed.
        # when it is empty, pop the first and push to the minheap.
        # have an end to record the current time, pop all the avail ones to minheap.
        # pop the ones with min cost time from the minheap, and update the end.
        # Time: O(nlogn), Space: O(n)
        minheap = []
        result = []
        cur_end = 0

        sorted_tasks = deque(sorted([(task[0], task[1], i) for i, task in enumerate(tasks)]))

        while minheap or sorted_tasks:
            # jump to next sorted_tasks if no minheap
            if not minheap and cur_end <= sorted_tasks[0][0]:
                cur_end = sorted_tasks[0][0]

            # Push all available tasks
            while sorted_tasks and sorted_tasks[0][0] <= cur_end:
                task = sorted_tasks.popleft()
                heapq.heappush(minheap, (task[1], task[2]))

            cost, i = heapq.heappop(minheap)
            cur_end += cost
            result.append(i)

        return result
            




        
