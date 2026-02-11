class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # topology sorting 
        # record the dst to source mapping
        # Time complexity O(V+E+E*V + Q), Space: O(V*V + E + Q)
        indegrees = {i:0 for i in range(numCourses)}
        adj_list = {i:[] for i in range(numCourses)}
        prep_list = {i: set() for i in range(numCourses)}
        for prep in prerequisites:
            src, dst = prep[0], prep[1]
            indegrees[dst] += 1
            adj_list[src].append(dst)

        q = deque([i for i in range(numCourses) if indegrees[i] == 0])
        while q:
            cur = q.popleft()
            for nei in adj_list[cur]:
                prep_list[nei].add(cur)
                #E*V, worst case prep_list[cur] could be O(V)
                prep_list[nei].update(prep_list[cur])
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        return [u in prep_list[v] for u, v in queries]

        
