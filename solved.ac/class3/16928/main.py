# https://www.acmicpc.net/problem/16928

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [0] * 101
for n in range(N+M):
    a, b = map(int, input().split())
    MAP[a] = b

def bfs():
    visited = [False] * 101
    queue = deque([(1, 0)])
    
    while queue:
        n, cnt = queue.popleft()
        
        if MAP[n] != 0:
            n = MAP[n]
        for i in range(1, 7):
            next_n = n+i
            if next_n < 100 and not visited[next_n]:
                queue.append((next_n, cnt+1))
                visited[next_n] = True
            elif next_n == 100:
                return cnt+1

print(bfs())