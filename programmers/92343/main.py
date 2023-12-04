# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    result = [False] * (len(info)+1)
    visited = [False] * len(info)
    graph = [ [] for _ in range(len(info)) ]
    for parent, child in edges:
        graph[parent].append(child)

    def dfs(sheep, wolf):
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True

                if info[child] == 0:
                    dfs(sheep+1, wolf)
                    result[sheep+1] = True
                elif sheep > wolf+1:
                    dfs(sheep, wolf+1)

                visited[child] = False

    visited[0] = True
    result[1] = True
    dfs(1, 0)
    for i in range(len(result)-1, -1, -1):
        if result[i]:
            return i

print(solution(
    [0,0,1,1,1,0,1,0,1,0,1,1],
    [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
))

print(solution(
    [0,1,0,1,1,0,1,0,0,1,0],
    [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
))