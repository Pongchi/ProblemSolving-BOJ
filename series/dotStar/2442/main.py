# https://www.acmicpc.net/problem/2442

N = int(input())
MAX = 2 * (N-1)
for i in range(N):
    print(' ' * (MAX//2 - i), end='')
    print('*' * (i * 2 + 1))