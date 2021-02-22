val = [4, 2, 10, 1, 2]
wt = [12, 1, 4, 1, 2]
W = 15
n = len(val)

dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]


def knapsack(W, n):
    print(W, n)
    if W == 0 or n == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]

    if wt[n - 1] > W:
        dp[n][W] = knapsack(W, n - 1)
        return dp[n][W]
    else:
        dp[n][W] = max(
            knapsack(W, n - 1),
            val[n - 1] + knapsack(W - wt[n - 1], n - 1)
        )
        return dp[n][W]


print(knapsack(W, n))

for i in dp:
    print(i)
