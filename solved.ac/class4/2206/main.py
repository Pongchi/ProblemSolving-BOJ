# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
MAP = [ list(map(int, input().rstrip())) for _ in range(N) ]

walls = [(0, 0)]
for i in range(N):
    for j in range(M):
        if MAP[i][j]:
            walls.append((i, j))

def bfs():
    queue = deque([(0, 0, 1)])
    visited = [ [False] * M for _ in range(N) ]
    visited[0][0] = True
    while queue:
        current_x, current_y, distance = queue.popleft()
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and MAP[next_x][next_y] == 0 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, distance+1))
                if next_x == N-1 and next_y == M-1:
                    return distance+1

    return float('inf')

result = float('inf')
for wall_x, wall_y in walls:
    MAP[wall_x][wall_y] = 0
    result = min(result, bfs())
    MAP[wall_x][wall_y] = 1

print(result != float('inf') and result or -1)