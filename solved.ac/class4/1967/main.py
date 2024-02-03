# https://www.acmicpc.net/problem/1967

import sys

sys.setrecursionlimit(10**5)

lines = sys.stdin.readlines()

n = int(lines[0])
graph = [ [] for _ in range(n+1) ]
for line in lines[1:]:
    a, b, c = map(int, line.split())
    graph[a].append((b, c))

diameters = [0] * (n+1)
def dfs(parent):
    result = []
    for child, weight in graph[parent]:
        result.append(dfs(child)+weight)

    diameters[parent] = max(result + [0])
    return diameters[parent]

dfs(1)
result = 0
for parent in range(1, n+1):
    tmp = sorted([diameters[child] + weight for child, weight in graph[parent]])
    result = max(result, sum(tmp[:2]))

print(result)