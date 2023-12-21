# https://www.acmicpc.net/problem/14500

import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
MAP = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]
max_value = max(map(max, MAP))
result = 0

def dfs(x, y, length, total):
    global result
    if result > total + max_value*(4-length):
        return

    if length == 4:
        result = max(result, total)
        return
    
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            dfs(next_x, next_y, length+1, total+MAP[next_x][next_y])
            if length == 2:
                dfs(x, y, length+1, total+MAP[next_x][next_y])
            visited[next_x][next_y] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, MAP[i][j])
        visited[i][j] = False

print(result)