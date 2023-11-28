# https://school.programmers.co.kr/learn/courses/30/lessons/72416

import heapq

def solution(sales, links):
    graph = [ [] for i in range(len(sales)+1) ]
    for a, b in links:
        graph[a].append(b)

    teams = []
    for i in range(len(sales)+1):
        if len(graph[i]) > 0:
            teams.append([i]+graph[i])

    result = set()
    for team in teams:
        member = min(team, key=lambda x : sales[x-1])
        result.add(member)
    
    print(result)
    return sum([ sales[member-1] for member in result ])

print(solution(
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
    [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
), 44)

# print(solution(
#     [5, 6, 5, 3, 4],
#     [[2,3], [1,4], [2,5], [1,2]]    
# ), 6)

# print(solution(
#     [5, 6, 5, 1, 4],
#     [[2,3], [1,4], [2,5], [1,2]]
# ), 5)

# print(solution(
#     [10, 10, 1, 1],
#     [[3,2], [4,3], [1,4]]
# ), 2)