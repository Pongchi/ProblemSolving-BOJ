# https://www.acmicpc.net/problem/12015

import sys
from bisect import bisect_left

input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))
dp = [seq[0]]

for i in range(1, A):
    if dp[-1] < seq[i]:
        dp.append(seq[i])
    else:
        idx = bisect_left(dp, seq[i])
        dp[idx] = seq[i]

print(len(dp))