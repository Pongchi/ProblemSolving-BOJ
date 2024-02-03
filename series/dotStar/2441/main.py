# https://www.acmicpc.net/problem/2441

N = int(input())
for i in range(N, 0, -1):
    whitespace = N - i
    print(whitespace * ' ' + i * '*')