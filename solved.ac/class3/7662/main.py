# https://www.acmicpc.net/problem/7662

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

for T in range(int(input())):
    minQ = []
    maxQ = []
    k = int(input())
    visited = [False] * k

    for K in range(k):
        cmd, value = input().split()
        value = int(value)
        if cmd == 'I':
            heappush(minQ, (value, K))
            heappush(maxQ, (-value, K))

        else:
            if value == 1:
                while maxQ and visited[ maxQ[0][1] ]:
                    heappop(maxQ)
                if not maxQ: continue
                n, idx = heappop(maxQ)
                visited[idx] = True

            else:
                while minQ and visited[ minQ[0][1] ]:
                    heappop(minQ)
                if not minQ: continue
                n, idx = heappop(minQ)
                visited[idx] = True

    while maxQ and visited[ maxQ[0][1] ]:
        heappop(maxQ)
    while minQ and visited[ minQ[0][1] ]:
        heappop(minQ)

    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print("EMPTY")

