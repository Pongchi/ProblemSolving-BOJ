# https://www.acmicpc.net/problem/6064

import sys

input = sys.stdin.readline

for T in range(int(input())):
    M, N, x, y = map(int, input().split())
    X, Y = (1, 1)
    result = 1

    while not (X == x and Y == y):
        result += 1
        X = X+1 if X < M else 1
        Y = Y+1 if Y < N else 1

        if X == M and Y == N:
            result = -1
            break

    print('답 :', result)