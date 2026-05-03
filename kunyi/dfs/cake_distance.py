## Step 1. Two pointers O(N) #####

def nearest_cake_distance(A: list[int], start: int) -> int:
    distance = float("inf")
    n = len(A)
    l, r = start, start

    while l >= 0:
        if A[l] == 1:
            distance = min(distance, abs(start - l))
            break

        l -= 1

    while r <= n - 1:
        if A[r] == 1:
            distance = min(distance, abs(start - r))
            break

        r += 1

    return -1 if distance == float("inf") else int(distance)
        
    

# --- Test Run ---
A = [0, 0, 1, 0, 0, 1, 0]
start = 0
try:
    result = nearest_cake_distance(A, start)
    print("Optimal Assignments (Person Index: Cake Index):")
    print(result)
except ValueError as e:
    print(e)

### step two Universal Optimization Pattern -> DFS + memo {state: minimum_cost}

from functools import lru_cache

def assign_cakes_globally(line: list[int]) -> dict[int, int]:
    # 1. Extract indices for persons and cakes
    p_indices = [i for i, v in enumerate(line) if v == 1]
    c_indices = [i for i, v in enumerate(line) if v == 2]

    num_p = len(p_indices)
    num_c = len(c_indices)

    if num_p > num_c:
        raise ValueError("impossible: fewer cakes than persons")
    if num_p == 0:
        return {}

    # 2. Use memoization to store (p_idx, c_idx) -> min_distance
    # choice_map stores whether we 'took' the cake at this state for backtracking
    choice_map = {}

    @lru_cache(None)
    def solve(p_i, c_i):
        # Base Case: All persons are paired
        if p_i == num_p:
            return 0
        # Base Case: Out of cakes but persons remain
        if c_i == num_c:
            return float('inf')

        # Choice 1: Pair person p_i with cake c_i
        dist = abs(p_indices[p_i] - c_indices[c_i])
        take_cost = dist + solve(p_i + 1, c_i + 1)

        # Choice 2: Skip this cake and try the next one for person p_i
        skip_cost = solve(p_i, c_i + 1)

        # Store the decision for backtracking later
        if take_cost <= skip_cost:
            choice_map[(p_i, c_i)] = True
            return take_cost
        else:
            choice_map[(p_i, c_i)] = False
            return skip_cost

    # Calculate global minimum
    total_min_dist = solve(0, 0)
    
    # 3. Backtrack to build the assignment map
    assignments = {}
    curr_p, curr_c = 0, 0
    
    while curr_p < num_p and curr_c < num_c:
        # Check the decision we made at this state
        if choice_map.get((curr_p, curr_c), False):
            # We paired them
            assignments[p_indices[curr_p]] = c_indices[curr_c]
            curr_p += 1
            curr_c += 1
        else:
            # We skipped this cake
            curr_c += 1

    return assignments

# --- Test Run ---
line_data = [1, 2, 0, 1, 0, 0, 2]
try:
    result = assign_cakes_globally(line_data)
    print("Optimal Assignments (Person Index: Cake Index):")
    print(result)
except ValueError as e:
    print(e)
