def construir_dp(C:list)->list:
    n = len(C)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        dp[i][i+1] = C[i]
    return dp

def maxGameResult(C:list)->float:
    n = len(C)
    dp = construir_dp(C)
    for d in range(1,n):
        for i in range(1,n-d+1):
            j = d+i
            s_1 = C[i-1] + min(dp[i+1][j],dp[i][j-1])
            s_2 = C[j-1] + min(dp[i-1][j-2],dp[i][j-1])
            dp[i-1][j] = max(s_1,s_2)
    return dp[0][n]

C= [5,3,7,10]
print(maxGameResult(C))