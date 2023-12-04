# https://www.acmicpc.net/problem/1949

import sys
sys.setrecursionlimit(10**4+1)
input = sys.stdin.readline

N = int(input())
vilages = [0] + list(map(int, input().split()))
graph = [ [] for _ in range(N+1) ]
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

# [선정안됬을때, 선정되었을때]
dp = [ [0, vilages[vilage]] for vilage in range(N+1) ]
visited = [False for _ in range(N+1)]

def dfs(node):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            dp[node][1] += dp[child][0]
            dp[node][0] += max(dp[child])

dfs(1)
print(max(dp[1]))