# https://www.acmicpc.net/problem/11722

import sys
from bisect import bisect_left

input = sys.stdin.readline

A = int(input())
seq = list(map(lambda x : -int(x), input().split()))

lis = [seq[0]]

for i in range(1, A):
    if lis[-1] < seq[i]:
        lis.append(seq[i])
    else:
        idx = bisect_left(lis, seq[i])
        lis[idx] = seq[i]

print(len(lis))