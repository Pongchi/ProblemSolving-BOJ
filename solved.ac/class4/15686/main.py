# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
MAP = [ list(map(int, input().split())) for _ in range(N) ]

homes = []
chicken_restaurants = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            homes.append((i, j))
        elif MAP[i][j] == 2:
            chicken_restaurants.append((i, j))

memo_chicken_restaurants = { (x, y) : [] for x, y in homes }
def get_chicken_distance(home_x, home_y):
    for chicken_x, chicken_y in sorted(memo_chicken_restaurants[(home_x, home_y)], key=lambda c : abs(home_x-c[0]) + abs(home_y-c[1])):
        if MAP[chicken_x][chicken_y] == 3:
            return abs(home_x - chicken_x) + abs(home_y - chicken_y)

    queue = deque([(home_x, home_y)])
    visited = [ [False] * N for _ in range(N) ]
    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

                if MAP[next_x][next_y] == 3:
                    memo_chicken_restaurants[(home_x, home_y)].append((next_x, next_y))
                    return abs(home_x - next_x) + abs(home_y - next_y)

    return float('inf')

result = float('inf')
for chicken_count in range(1, M+1):
    for alive_chicken_restaurants in combinations(chicken_restaurants, M):
        for chicken_x, chicken_y in alive_chicken_restaurants:
            MAP[chicken_x][chicken_y] = 3

        tmp = 0
        for home_x, home_y in homes:
            tmp += get_chicken_distance(home_x, home_y)
        
        result = min(result, tmp)
        
        for chicken_x, chicken_y in alive_chicken_restaurants:
            MAP[chicken_x][chicken_y] = 2

print(result)