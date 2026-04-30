from collections import deque
class Solution:
    def parallelCourse(self, prerequisites, N):
        # cases 1. A -> B; A -> C, E -> D (semester = 2); 2. A -> B, A -> C, B -> C, semester = 3
        # create adj_list, indegree_list 
        # do level-order topology sorting -> find the longest path
        adj_list = {i: [] for i in range(N)}
        indegree_list = {i: 0 for i in range(N)}

        for u, v in prerequisites:
            adj_list[u].append(v)
            indegree_list[v] += 1

        q = deque()
        # enque all the source to the queu of which indegree = 0
        for i in range(N):
            if indegree_list[i] == 0:
                q.append(i)

        result = 0
        course_taken = 0
        while q:
            # level order
            qsize = len(q)
            for _ in range(qsize):
                course = q.popleft()
                course_taken += 1

                for nei in adj_list[course]:
                    indegree_list[nei] -= 1
                    if indegree_list[nei] == 0:
                        q.append(nei)

            result += 1

        return result if course_taken == N else -1

sol = Solution()
result = sol.parallelCourse([[0, 1], [0, 2], [3, 4]], 5)
print(f"result is {result}")

result = sol.parallelCourse([[0, 1], [0, 2], [1, 2]], 3)
print(f"result is {result}")

print(f"Case 3 (Cycle) Result: {sol.parallelCourse([[0, 1], [1, 0]], 2)}")
