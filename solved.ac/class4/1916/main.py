# https://www.acmicpc.net/problem/1916

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    start, dest, cost = map(int, input().split())
    graph[start].append((dest, cost))

def dijkstra(start, dest):
    costs = [ float('inf') for _ in range(N+1) ]
    costs[start] = 0
    queue = []
    heappush(queue, (costs[start], start))

    while queue:
        current_cost, current_viliage = heappop(queue)

        if costs[current_viliage] < current_cost:
            continue

        for vilage, cost in graph[current_viliage]:
            new_cost = current_cost + cost
            if new_cost < costs[vilage]:
                costs[vilage] = new_cost
                heappush(queue, (new_cost, vilage))

    return costs[dest]

A, B = map(int, input().split())
print(dijkstra(A, B))