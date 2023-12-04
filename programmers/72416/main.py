# https://school.programmers.co.kr/learn/courses/30/lessons/72416

import sys
sys.setrecursionlimit(10**6)

def solution(sales, links):
    N = len(sales)
    graph = [ [] for _ in range(N+1) ]
    for U, V in links:
        graph[U].append(V)

    # [워크샵 불참여, 참여]
    dp = [[0, 0]] + [ [0, sales[employee]] for employee in range(N) ]
    def dfs(node):
        if not graph[node]: return
        
        min_cost = float('inf')
        for child in graph[node]:
            dfs(child)

            dp[node][0] += min(dp[child])
            dp[node][1] += min(dp[child])
            if dp[child][0] < dp[child][1]:
                min_cost = min(min_cost, dp[child][1] - dp[child][0])
            else:
                min_cost = 0

        dp[node][0] += min_cost
    
    dfs(1)
    return min(dp[1])

print(solution(
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
    [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
), 44)

print(solution(
    [5, 6, 5, 3, 4],
    [[2,3], [1,4], [2,5], [1,2]]    
), 6)

print(solution(
    [5, 6, 5, 1, 4],
    [[2,3], [1,4], [2,5], [1,2]]
), 5)

print(solution(
    [10, 10, 1, 1],
    [[3,2], [4,3], [1,4]]
), 2)