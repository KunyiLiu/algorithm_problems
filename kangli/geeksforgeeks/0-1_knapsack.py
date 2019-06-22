def zero_one_knapsack(values, weights, w):
    n = len(values)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values[i-1]+dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
t = int(input())
for i in range(t):
    n = input()
    w = int(input())
    values = [int(x) for x in input().split()]
    weights = [int(y) for y in input().split()]
    print(zero_one_knapsack(values, weights, w))

'''
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines.
The first line consists of N the number of items.
The second line consists of W, the maximum capacity of the knapsack.
In the next line are N space separated positive integers denoting the values of the N items,
and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.

Output:
For each testcase, in a new line, print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ v[i] ≤ 1000

Example:
Input:
1
3
4
1 2 3
4 5 1
Output:
3

** For More Input/Output Examples Use 'Expected Output' option **
Author: Hemang Sarkar

For Input:
2
28
83
55 61 51 75 17 22 4 13 39 28 77 49 46 91 14 67 88 62 25 37 69 38 59 62 48 88 100 53 
96 16 34 53 88 6 50 26 76 10 8 4 37 18 73 54 30 31 97 2 28 24 2 30 79 77 33 86 
16
98
20 16 45 73 99 87 38 53 99 99 38 65 22 17 17 51 
31 21 78 53 18 66 61 4 11 65 16 99 87 91 44 23
Output of Online Judge is:
474
356
'''
