class Solution:
    """
    @param courses: duration and close day of each course
    @return: the maximal number of courses that can be taken
    """
    def scheduleCourse(self, courses):
        """
        贪心法 Greedy
课程按照 deadline 排序，从左到右扫描每个课程，依次学习。如果发现学了之后超过 deadline 的，就从之前学过的课程里扔掉一个耗时最长的。
因为这样可以使得其他的课程往前挪，而往前挪是没影响的。
所以挑最大值这个事情就是 Heap 的事情了
        """
        import heapq
        
        cur_time = 0
        heap = []
        courses = sorted(courses, key=lambda x: x[1])
        for duration, ddl in courses:
            cur_time += duration
            heapq.heappush(heap, -duration)
            if cur_time > ddl:
                max_duration = - heapq.heappop(heap)
                cur_time -= max_duration
                
        return len(heap)
