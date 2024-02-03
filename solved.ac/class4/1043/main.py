# https://www.acmicpc.net/problem/1043

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
knowns = set(map(int, input().split()[1:]))
parties = [ set(map(int, input().split()[1:])) for _ in range(M) ]

for _ in range(M):
    for party in parties:
        if knowns.intersection(party):
            knowns.update(party)

result = 0
for party in parties:
    if len( knowns.intersection(party) ) == 0:
        result += 1

print(result)