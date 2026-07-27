dependencies = [
    ("A", ["E", "B"]),  
    ("E", ["C"]),              
    ("B", ["C"]),              
    ("C", []),                        
    ("F", ["G", "E"]),  
    ("G", []),                        
]

targets = ["A", "F"]

# topologing sorting 
# 1. transfer dependencies to adj_list with ind_map, parent_to_child, child_to_parent 
# 2. queue of targets to get the required course 
# 3. use Kahn algorithm to start from ind = 0 of the required courses

from collections import defaultdict, deque
def solution(dependencies, targets):
    ind_list = defaultdict(int)
    parent_to_child = defaultdict(list)
    child_to_parent = defaultdict(list)
    node_set = set()

    for child, parents in dependencies:
        child_to_parent[child].extend(parents)
        node_set.add(child)
        for p in parents:
            parent_to_child[p].append(child)
            ind_list[child] += 1
            node_set.add(p)

    q = deque(targets)
    required_nodes = set(targets)
    while q:
        node = q.popleft()
        for p in child_to_parent[node]:
            if p not in required_nodes:
                required_nodes.add(p)
                q.append(p)

    # Kahn algorithm
    sources = [node for node in required_nodes if ind_list[node] == 0]
    q = deque(sources)
    path = []
    while q:
        course = q.popleft()
        path.append(course)
        
        for child in parent_to_child[course]:
            ind_list[child] -= 1 
            if ind_list[child] == 0:
                q.append(child)

    if len(path) < len(required_nodes):
        raise ValueError("Cycle exists")

    return path

result = solution(dependencies, targets)
print(result)


# DFS visiting + visited

from collections import defaultdict
def solution(dependencies, targets):
    parent_to_child = defaultdict(list)
    child_to_parent = defaultdict(list)
    for child, parents in dependencies:
        child_to_parent[child].extend(parents)
        for p in parents:
            parent_to_child[p].append(child)

    path = []
    # fully processed courses
    visited = set()
    # courses currently in recursion stack like A -> E -> C;
    # only when its dependencies are fully processed, it can be added to visited
    visiting = set()

    def dfs(node):
        if node in visited:
            return 

        if node in visiting:
            raise ValueError("Cycle Exists")

        visiting.add(node)
        for parent in child_to_parent[node]:
            dfs(parent)

        visiting.remove(node)
        visited.add(node)
        path.append(node)
        
        return

    for target in targets:
        dfs(target)

    return path

result = solution(dependencies, targets)
print(result)
