# https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq

def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = { i: {} for i in range (1, n+1) }
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    def dijkstra(start, end):
        costs = [ float('inf') for i in range(n+1) ]
        costs[start] = 0
        queue = []
        heapq.heappush(queue, [costs[start], start])

        while queue:
            current_cost, current_loc = heapq.heappop(queue)
            if (costs[current_loc] < current_cost):
                continue

            for new_loc, new_cost in graph[current_loc].items():
                cost = current_cost + new_cost
                if cost < costs[new_loc]:
                    costs[new_loc] = cost
                    heapq.heappush(queue, [cost, new_loc])
        
        return costs[end]

    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return answer

print(solution(
    6,
    4,
    6,
    2,
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
) == 82)

print(solution(
    7,
    3,
    4,
    1,
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
) == 14)

print(solution(
    6,
    4,
    5,
    6,
    [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
) == 18)