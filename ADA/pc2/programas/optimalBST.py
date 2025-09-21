import math
import utils

def construir_dp(V:list) -> list[list]:
    n = len(V)
    dp = [[0.0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        dp[i][i+1] = V[i]
    return dp

def construir_rtable(nodes:list)-> list[list]:
    n = len(nodes)
    rtable = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        rtable[i][i] = i
    return rtable


def optimalBST(K:list,V:list) -> tuple[float, list]:
    n = len(K)
    dp = construir_dp(V)
    rtable = construir_rtable(K)

    for d in range(1,n):
        for i in range(1,n-d+1):
            j = d+i
            min = math.inf
            for l in range(i,j+1):
                m = dp[i-1][l-1] + dp[l][j]
                if m < min:
                    rtable[i-1][j-1] = l-1
                    min = m
            for k in range (i,j+1):
                min+=V[k-1]
            dp[i-1][j] = min
    return (dp[0][n],rtable)

def reconstruir_arbol(rtable:list) ->utils.Tree:
    P = utils.Stack()
    n = len(rtable)
    root = utils.Node(key=rtable[0][n-1])
    P.push((root,0,n-1))
    l = []
    while(P.length()>0):
        l,i,j = P.pop()
        r = l.key
        if(i<r):
            v = utils.Node(key=rtable[i][r-1])
            l.left = v
            P.push((v,i,r-1))
        if(r<j):
            v = utils.Node(key=rtable[r+1][j])
            l.right=v
            P.push((v,r+1,j))

    return utils.Tree(root=root)

min_cost,rtable = optimalBST(['A','B','C','D','E'],[0.213,0.20,0.547,0.100,0.120])
tree = reconstruir_arbol(rtable)
print(min_cost)
print(tree.printAsList(labels=['A','B','C','D','E']))