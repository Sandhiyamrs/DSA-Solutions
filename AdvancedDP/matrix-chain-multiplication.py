import sys

def matrixChainOrder(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n - 1]
