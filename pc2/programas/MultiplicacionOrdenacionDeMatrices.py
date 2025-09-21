import math
def menor_numero_de_productos(p):
    n = len(p) - 1
    dp = [[0.0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = math.inf
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]

p = [10, 30, 5, 60]
print(menor_numero_de_productos(p))