# https://www.acmicpc.net/problem/1504

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, E = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    queue = [(0, start)]
    distances = [float('inf')] * (N+1)
    distances[start] = 0
    
    while queue:
        current_distance, current_location = heappop(queue)

        if distances[current_location] < current_distance:
            continue
        
        for next_location, next_distance in graph[current_location]:
            new_distance = current_distance + next_distance
            if new_distance < distances[next_location]:
                heappush(queue, (new_distance, next_location))
                distances[next_location] = new_distance

    return distances[end]

result = min(
    dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),
    dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
)
print(result != float('inf') and result or -1)