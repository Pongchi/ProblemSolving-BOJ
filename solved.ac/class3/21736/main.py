# https://www.acmicpc.net/problem/21736

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
MAP = [ input().rstrip() for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]

def find_doyeon():
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'I':
                return (i, j)

result = 0
dst_x, dst_y = find_doyeon()
visited[dst_x][dst_y] = True
queue = deque([(dst_x, dst_y)])

while queue:
    current_x, current_y = queue.popleft()
    for i in range(4):
        move_x = current_x+dx[i]
        move_y = current_y+dy[i]
        if 0 <= move_x < N and 0 <= move_y < M and MAP[move_x][move_y] != 'X' and not visited[move_x][move_y]:
            queue.append((move_x, move_y))
            visited[move_x][move_y] = True
            if MAP[move_x][move_y] == 'P':
                result += 1

print(result if result != 0 else "TT")