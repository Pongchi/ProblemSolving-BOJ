# https://www.acmicpc.net/problem/15663

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [False] * 10005
def dfs(arr):
    if len(arr) == M:
        print(*arr)
        return

    last_number = 0
    for i in range(N):
        if not visited[i] and last_number != numbers[i]:
            visited[i] = True
            last_number = numbers[i]
            arr.append(numbers[i])

            dfs(arr)

            visited[i] = False
            arr.pop()

dfs([])