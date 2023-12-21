# https://www.acmicpc.net/problem/6064

import sys

input = sys.stdin.readline

for T in range(int(input())):
    M, N, x, y = map(int, input().split())
    result = x

    max_year = M*N
    while result <= max_year and (result-y) % N != 0:
        result += M

    print(result <= max_year and result or -1)