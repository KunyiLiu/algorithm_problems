class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        import queue 
        queue = queue.Queue()
        result = []
        adjancy_list = {i: [] for i in range(numCourses)}
        ind_list = {i: 0 for i in range(numCourses)}
        for edge in prerequisites:
            adjancy_list[edge[0]].append(edge[1])
            ind_list[edge[1]] += 1 
            
        for ind in ind_list:
            if ind_list[ind] == 0:
                queue.put(ind)
                
        while not queue.empty():
            node = queue.get()
            result.append(node)
            for neighbor in adjancy_list[node]:
                ind_list[neighbor] -= 1 
                if ind_list[neighbor] == 0:
                    queue.put(neighbor)
                    
                    
        return len(result) == numCourses
