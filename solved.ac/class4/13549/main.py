# https://www.acmicpc.net/problem/13549

from collections import deque

N, K = map(int, input().split())
dp = [-1] * 100005

def bfs():
    queue = deque([[0, N]])
    while queue and dp[K] == -1:
        time, current_location = queue.popleft()
        
        if 0 <= current_location*2 <= 100000 and dp[current_location*2] == -1:
            queue.append([time, current_location*2])
            dp[current_location*2] = time
        
        if 0 <= current_location-1 <= 100000 and dp[current_location-1] == -1:
            queue.append([time+1, current_location-1])
            dp[current_location-1] = time+1

        if 0 <= current_location+1 <= 100000 and dp[current_location+1] == -1:
            queue.append([time+1, current_location+1])
            dp[current_location+1] = time+1

bfs()
print(dp[K])