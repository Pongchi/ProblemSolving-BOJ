# https://www.acmicpc.net/problem/1238

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    src, dst, cost = map(int, input().split())
    graph[src].append((dst, cost))

def dijkstra(root):
    distances = [float('inf')] * (N+1)
    distances[root] = 0

    queue = []
    heappush(queue, (0, root))

    while queue:
        cost, src = heappop(queue)

        if distances[src] < cost:
            continue

        for dst, next_cost in graph[src]:
            new_cost = cost + next_cost
            if new_cost < distances[dst]:
                distances[dst] = new_cost
                heappush(queue, (new_cost, dst))

    return distances

come_backs = dijkstra(X)
goes = [0] + [ dijkstra(i)[X] for i in range(1, N+1) ]

result = 0
for i in range(1, N+1):
    tmp = goes[i] + come_backs[i]
    if result < tmp:
        result = tmp

print(result)