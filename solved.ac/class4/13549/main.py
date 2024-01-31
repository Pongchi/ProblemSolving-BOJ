# https://www.acmicpc.net/problem/13549

from collections import deque

N, K = map(int, input().split())
dp = [-1] * 100005

def bfs():
    queue = deque([N])
    dp[N] = 0
    while queue and dp[K] == -1:
        current_location = queue.popleft()
        
        if 0 <= current_location*2 <= 100000 and dp[current_location*2] == -1:
            queue.append(current_location*2)
            dp[current_location*2] = dp[current_location]
        
        if 0 <= current_location-1 <= 100000 and dp[current_location-1] == -1:
            queue.append(current_location-1)
            dp[current_location-1] = dp[current_location] + 1

        if 0 <= current_location+1 <= 100000 and dp[current_location+1] == -1:
            queue.append(current_location+1)
            dp[current_location+1] = dp[current_location] + 1

bfs()
print(dp[K])