# https://www.acmicpc.net/problem/14002

import sys
from bisect import bisect_left

input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(A)]

for i in range(1, A):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)

lis = []
max_lis_length = max(dp)
target = max_lis_length
idx = A-1
while target > 0:
    if dp[idx] == target:
        target -= 1
        lis.append(seq[idx])
    idx -= 1

print(max_lis_length)
print(*lis[::-1])