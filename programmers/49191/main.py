# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    WIN, MYSTERY, LOSE = [1, 0, -1]
    graph = [ [MYSTERY] * (n+1) for _ in range(n+1) ]
    for A, B in results:
        graph[A][B] = WIN
        graph[B][A] = LOSE

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if WIN == graph[i][k] == graph[k][j]:
                    graph[i][j] = WIN
                    graph[j][i] = LOSE
    
    result = 0
    for i in range(1, n+1):
        if graph[i].count(MYSTERY) == 2:
            result += 1
    return result

print(solution(
    5,
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
), 2)