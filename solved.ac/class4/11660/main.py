# https://www.acmicpc.net/problem/11660

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [ list(map(int, input().split())) for _ in range(N) ]

for i in range(N):
    for j in range(1, N):
        MAP[i][j] += MAP[i][j-1]

def range_sum(x1, y1, x2, y2):
    result = 0
    for i in range(x1, x2+1):
        if y1 != 0:
            result += MAP[i][y2] - MAP[i][y1-1]
        else:
            result += MAP[i][y2]
    return result

for i in range(M):
    print(range_sum(*map(lambda x : int(x)-1, input().split())))