"""
Problem Requirements
We have n courses labeled from 1 to n. We are given two lists of data:

relations: This list shows which courses are required for others. An item [prevCourse, nextCourse] means you must finish prevCourse before you can start nextCourse.
time: This is a 1-indexed array where time[i] shows how many months the (i + 1)th course takes to complete.
You can take multiple courses at the same time (in parallel) if you have finished all their required courses.

We need to return the minimum number of months it takes to finish every course.

Sample Cases
Example 1:

Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]

Output: 8

Explanation:

Course 1 and Course 2 do not have any requirements. We can start them both immediately.
Course 1 takes 3 months. Course 2 takes 2 months.
By month 3, both courses are done.
Course 3 requires both Course 1 and Course 2 to be finished. So, Course 3 starts at month 3.
Course 3 takes 5 months.
Total time = 3 (wait for requirements) + 5 (course duration) = 8 months.
Example 2:

Input: n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]

Output: 12

Technical Limits
1 <= n <= 5 * 10^4 (Up to 50,000 courses).
The relations array size is between 0 and 50,000.
Each relation contains exactly 2 items.
1 <= prevCourse, nextCourse <= n
A course cannot be a requirement for itself (prevCourse != nextCourse).
The graph is a Directed Acyclic Graph (DAG), meaning there are no loops.
1 <= time[i] <= 10^4 (Each course takes up to 10,000 months).
"""
from collections import deque
def get_parallel_courseIII(n, relations, time):
    dp = [0] * n # earliest finish time for course i (all dependency finish)
    adj_list = {i: [] for i in range(n)}
    indegree_list = {i:0 for i in range(n)}

    for u,v in relations:
        u -= 1
        v -= 1
        adj_list[u].append(v)
        indegree_list[v] += 1

    q = deque()
    for i in range(n):
        if indegree_list[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        course = q.popleft()
        for nei in adj_list[course]:
            # course is nei's dependency to finish
            dp[nei] = max(dp[nei], dp[course] + time[nei])
            indegree_list[nei] -= 1
            if indegree_list[nei] == 0:
                q.append(nei)

    return max(dp)
    

n = 5
relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time = [1,2,3,4,5]
result = get_parallel_courseIII(n, relations, time)
print(f"1st result is {result}")

n = 3
relations = [[1,3],[2,3]]
time = [100, 1, 1]
result = get_parallel_courseIII(n, relations, time)
print(f"2nd result is {result}")
