# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
MAP = [ list(map(int, input().rstrip())) for _ in range(N) ]

def bfs():
    queue = deque([(0, 0, 0)])
    visited = [ [[0] * 2 for j in range(M)] for i in range(N) ]
    visited[0][0][0] = 1

    while queue:
        current_x, current_y, isBreak = queue.popleft()
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y][isBreak]:
                if next_x == N-1 and next_y == M-1:
                    return visited[current_x][current_y][isBreak] + 1

                if MAP[next_x][next_y] == 0:
                    visited[next_x][next_y][isBreak] = visited[current_x][current_y][isBreak] + 1
                    queue.append((next_x, next_y, isBreak))
                
                elif MAP[next_x][next_y] == 1 and isBreak == 0:
                    visited[next_x][next_y][1] = visited[current_x][current_y][isBreak] + 1
                    queue.append((next_x, next_y, 1))

    return -1

if N == 1 == M:
    print(1)
else:
    print(bfs())