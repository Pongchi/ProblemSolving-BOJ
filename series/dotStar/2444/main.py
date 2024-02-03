# https://www.acmicpc.net/problem/2444

N = int(input())
MAX = 2 * (N-1)

for i in range(N-1):
    print(' ' * (MAX//2 - i), end='')
    print('*' * (i * 2 + 1))

for i in range(N-1, -1, -1):
    print(' ' * (MAX//2 - i), end='')
    print('*' * (i * 2 + 1))