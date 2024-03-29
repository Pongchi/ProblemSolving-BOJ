# https://www.acmicpc.net/problem/14003

import sys
from bisect import bisect_left

input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))
lis = [-1000000001]
dp = [0] * A
dp[0] = 1

for i in range(A):
    if lis[-1] < seq[i]:
        lis.append(seq[i])
        dp[i] = len(lis) - 1
    else:
        idx = bisect_left(lis, seq[i])
        dp[i] = idx
        lis[idx] = seq[i]

max_len = max(dp)
print(max_len)

real_lis = []
for i in range(A-1, -1, -1):
    if dp[i] == max_len:
        real_lis.append(seq[i])
        max_len -= 1

print(*real_lis[::-1])