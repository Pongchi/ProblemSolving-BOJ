# https://www.acmicpc.net/problem/15681

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
print = sys.stdout.write

N, R, Q = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
count = [0] * (N+1)
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

def dfs(node):
    count[node] = 1
    for child in graph[node]:
        if not count[child]:
            dfs(child)
            count[node] += count[child]

dfs(R)
for _ in range(Q):
    print(f'{count[int(input())]}\n')