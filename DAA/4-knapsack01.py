def knapsack(W, wt, val, n):
    dp = [[0 for j in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

if __name__ == "__main__":
    val = [1, 2, 5, 6]
    wt = [2, 3, 4, 5]
    W = 8
    n = len(val)

    result = knapsack(W, wt, val, n)
    print("Maximum value:", result)

