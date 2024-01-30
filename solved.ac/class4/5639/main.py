# https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10**5)

keys = list(map(int, sys.stdin.readlines()))
def postorder(start, end):
    if start >= end: return

    point = end
    for i in range(start+1, end):
        if keys[start] < keys[i]:
            point = i
            break

    postorder(start+1, point)
    postorder(point, end)
    print(keys[start])

    return

postorder(0, len(keys))