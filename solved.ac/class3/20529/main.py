# https://www.acmicpc.net/problem/20529

import sys
from itertools import combinations

input = sys.stdin.readline

def calc_distance(a, b):
    result = 0
    for i in range(4):
        if a[i] != b[i]:
            result += 1
    return result

for T in range(int(input())):
    N = int(input())
    students = input().split()

    if N > 32: print(0)
    else:
        result = float('inf')
        for A, B, C in combinations(students, 3):
            tmp = calc_distance(A, B) + calc_distance(B, C) + calc_distance(A, C)
            result = min(result, tmp)
            if result == 0:
                break
        print(result)