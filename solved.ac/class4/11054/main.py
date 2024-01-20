# https://www.acmicpc.net/problem/11054

import sys
from bisect import bisect_left

input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))

lis = [seq[0]]
lis_dp = []
for i in range(A):
    if lis[-1] < seq[i]:
        lis.append(seq[i])
    else:
        idx = bisect_left(lis, seq[i])
        lis[idx] = seq[i]
    lis_dp.append(len(lis))

seq.reverse()

lds = [seq[0]]
lds_dp = []
for i in range(A):
    if lds[-1] < seq[i]:
        lds.append(seq[i])
    else:
        idx = bisect_left(lds, seq[i])
        lds[idx] = seq[i]
    lds_dp.append(len(lds))

result = 1
lds_dp.reverse()
for i in range(A):
    result = max(result, lis_dp[i] + lds_dp[i])

print(result-1)