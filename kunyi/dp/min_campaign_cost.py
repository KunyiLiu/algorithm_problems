# Dp[w][i] - min cost of assiging campagn i for week w
# base: dp[0][0] = 0, dp[w][0] = inf, dp[0][i] = inf
# edge: dp[w][i] = min(dp[w-1][j] + max(cost j .. i))
# result: dp[weeks][n]

def min_campaign_cost(costs, weeks):
    # corner case, if week = 1, then result is max(costs)
    # if costs < weeks then -1 
    n = len(costs)
    if n < weeks:
        return -1 

    dp = [[float("inf")] * (n + 1) for _ in range(weeks + 1)]
    dp[0][0] = 0

    for w in range(1, weeks + 1):
        # each week at least have 1 campagain
        for i in range(w, n + 1):
            # compare with the last dp[w-1], j from w - 1 to i - 1
            max_cost = 0
            # reverse, ensure getting the max cost from cost[j .. i - 1]
            for j in range(i-1, w - 2, -1):
                max_cost = max(max_cost, costs[j])
                dp[w][i] = min(dp[w][i], dp[w-1][j] + max_cost)

    return dp[weeks][n]
    
costs = [2, 5, 4, 3, 7, 1, 6, 8]
weeks = 3
print(f"result is {min_campaign_cost(costs, weeks)}")

def min_campaign_cost_space(costs, weeks):
    # corner case, if week = 1, then result is max(costs)
    # if costs < weeks then -1 

    if len(costs) < weeks:
        return -1 

    c_len = len(costs)
    prev_dp = [float("inf")] * (c_len + 1)
    prev_dp[0] = 0

    for w in range(1, weeks + 1):
        # each week need at least 1 campagin
        cur_dp = [float("inf")] * (c_len + 1)
        for i in range(w, c_len + 1):
            # compare with the dp[w-1][j], j must >= w - 1
            # at least leave 1 campagain for wth week
            cur_max = 0
            for j in range(i - 1, w - 2, -1):
                cur_max = max(cur_max, costs[j])
                cur_dp[i] = min(cur_dp[i], prev_dp[j] + cur_max)
        prev_dp = cur_dp
    
    return prev_dp[c_len]


costs = [2, 5, 4, 3, 7, 1, 6, 8]
weeks = 3
print(f"result is {min_campaign_cost_space(costs, weeks)}")
