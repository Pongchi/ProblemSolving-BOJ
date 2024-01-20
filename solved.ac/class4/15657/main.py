# https://www.acmicpc.net/problem/15657

from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for sequence in combinations_with_replacement(numbers, M):
    print(*sequence)