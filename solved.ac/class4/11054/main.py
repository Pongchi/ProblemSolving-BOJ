# https://www.acmicpc.net/problem/11054

import sys
from bisect import bisect_left

input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))

lis = [seq[0]]
lis_dp = [0] * A
for i in range(A):
    if lis[-1] < seq[i]:
        lis.append(seq[i])
        lis_dp[i] = len(lis)
    else:
        idx = bisect_left(lis, seq[i])
        lis[idx] = seq[i]
        lis_dp[i] = idx

minus_seq = list(map(lambda x : -x, seq))

lds = [minus_seq[0]]
lds_dp = [0] * A
for i in range(A):
    if lds[-1] < minus_seq[i]:
        lds.append(minus_seq[i])
        lds_dp[i] = len(lds)
    else:
        idx = bisect_left(lds, minus_seq[i])
        lds[idx] = minus_seq[i]
        lds_dp[i] = idx

result = 1
for i in range(A):
    result = max(result, lis_dp[i] + lds_dp[i])

print(result-1)