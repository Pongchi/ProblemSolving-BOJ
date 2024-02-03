# https://www.acmicpc.net/problem/1967

import sys

sys.setrecursionlimit(10**5)

lines = sys.stdin.readlines()

n = int(lines[0])
graph = [ [] for _ in range(n+1) ]
for line in lines[1:]:
    a, b, c = map(int, line.split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def calc_distances_from(start):
    distances = [-1] * (n+1)
    distances[start] = 0
    def dfs(parent, distance):
        for child, weight in graph[parent]:
            if distances[child] == -1:
                distances[child] = distance + weight
                dfs(child, distances[child])

    dfs(start, 0)
    return distances

distances = calc_distances_from(1)
start = distances.index(max(distances))
print(max(calc_distances_from(start)))