# https://www.acmicpc.net/problem/17070

import sys

input = sys.stdin.readline

N = int(input())
MAP = [ list(map(int, input().split())) for _ in range(N) ]
dp = [ [ [0, 0, 0] for __ in range(N) ]  for _ in range(N) ]

dp[0][1][0] = 1
for column in range(2, N):
    if MAP[0][column] == 0:
        dp[0][column][0] = dp[0][column-1][0]

for i in range(1, N):
    for j in range(1, N):
        if MAP[i][j] == 0:
            # 가로
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]

            # 세로
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

            # 대각선
            if 0 == MAP[i-1][j] == MAP[i][j-1]:
                dp[i][j][2] = sum(dp[i-1][j-1])


print(sum(dp[N-1][N-1]))