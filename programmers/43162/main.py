# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    visited = [False for i in range(n)]
    stack = []
    result = 0
    for i in range(n):
        if not visited[i]:
            result += 1
            visited[i] = True
            stack.append(i)

            while stack:
                visit_node = stack.pop()
                for j in range(n):
                    if not visited[j] and i != j and computers[visit_node][j]:
                        stack.append(j)
                        visited[j] = True
        
    return result

print(solution(
    3,
    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
), 2)

print(solution(
    3,
    [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
), 1)