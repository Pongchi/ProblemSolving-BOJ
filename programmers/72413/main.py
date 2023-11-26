# https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq

def solution(n, s, a, b, fares):
    INF = float('inf')
    graph = { i: {} for i in range (1, n+1) }
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f

    costs = [ [INF] * (n+1) for i in range(n+1) ]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == j):
                costs[i][j] = 0
            else:
                costs[i][j] = graph[i].get(j, INF)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                costs[i][j] = min(costs[i][k] + costs[k][j], costs[i][j])

    answer = INF
    for i in range(1, n+1):
        answer = min(costs[s][i] + costs[i][a] + costs[i][b], answer)

    return answer

print(solution(
    6,
    4,
    6,
    2,
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
))

print(solution(
    7,
    3,
    4,
    1,
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
))

print(solution(
    6,
    4,
    5,
    6,
    [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
))