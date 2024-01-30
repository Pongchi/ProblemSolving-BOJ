# https://www.acmicpc.net/problem/2096

import sys

input = sys.stdin.readline

N = int(input())
max_result = [0, 0, 0]
min_result = [0, 0, 0]

for row in range(N):
    rows = list(map(int, input().split()))
    temp = max_result[:]
    max_result[0] = max(rows[0]+temp[0], rows[1]+temp[1])
    max_result[1] = max(rows[0]+temp[0], rows[1]+temp[1], rows[2]+temp[2])
    max_result[2] = max(rows[1]+temp[1], rows[2]+temp[2])

    temp = min_result[:]
    min_result[0] = min(rows[0]+temp[0], rows[1]+temp[1])
    min_result[1] = min(rows[0]+temp[0], rows[1]+temp[1], rows[2]+temp[2])
    min_result[2] = min(rows[1]+temp[1], rows[2]+temp[2])

print(max(max_result), min(min_result))