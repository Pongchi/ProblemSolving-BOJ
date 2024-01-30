# https://www.acmicpc.net/problem/15666

N, M = map(int, input().split())
numbers = list(set(map(int, input().split())))
numbers.sort()

def dfs(arr, start_index):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start_index, len(numbers)):
        arr.append(numbers[i])

        dfs(arr, i)

        arr.pop()

dfs([], 0)