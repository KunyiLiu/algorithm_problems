class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap based on occurence count => tasks that are ready to run right now
        # queue -> cool down queue.
        # pop the max count first, and after this (task, count) is poped,
        # make count -= 1 and wait for n cycles to heappush it back.
        # continue the operations until heap and wait dictionary is empty
        # level order traversal
        # Time complexity O(N) where N is the number of tasks


        import heapq
        from collections import Counter, deque
        task_count = Counter(tasks)
        heap = [(-cnt, task) for task, cnt in task_count.items()]
        heapq.heapify(heap)

        q = deque()  # task -> next available time
        time = 0

        while heap or q:
            time += 1

            # check if there is task finish cooldown
            while q and q[0][1] <= time:
                task = q.popleft()[0]
                heapq.heappush(heap, (-task_count[task], task))

            if heap:
                task = heapq.heappop(heap)[1]
                task_count[task] -= 1
                if task_count[task] > 0:
                    # if there is next task to run, add it to cooldown queue
                    q.append((task, n + time + 1))

        return time

        
        
