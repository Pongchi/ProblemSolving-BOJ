# https://www.acmicpc.net/problem/15663

from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for sequence in permutations(numbers, M):
    print(*sequence)