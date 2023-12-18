# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
MAP = [ list(map(int, input().split())) for _ in range(n) ]
result = [ [0] * m for _ in range(n) ]

def find_dst():
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 2:
                return (i, j)

def bfs():
    dst_x, dst_y = find_dst()
    queue = deque([(dst_x, dst_y, 0)])

    while queue:
        current_x, current_y, distance = queue.popleft()
        for i in range(4):
            move_x = current_x+dx[i]
            move_y = current_y+dy[i]
            if 0 <= move_x < n and 0 <= move_y < m and MAP[move_x][move_y] == 1 and result[move_x][move_y] == 0:
                result[move_x][move_y] = distance+1
                queue.append((move_x, move_y, distance+1))

    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 1 and result[i][j] == 0:
                result[i][j] = -1
bfs()
for i in range(n):
    print(*result[i])