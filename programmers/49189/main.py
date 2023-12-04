from collections import deque

def solution(n, edge):
    result = [0] * (n+1)
    graph = [ [] for _ in range(n+1) ]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])
    while queue:
        now = queue.popleft()
        
        for next_node in graph[now]:
            if not result[next_node]:
                queue.append(next_node)
                result[next_node] = result[now] + 1

    return result[2:].count(max(result[2:]))

print(solution(
    6,
    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
), 3)