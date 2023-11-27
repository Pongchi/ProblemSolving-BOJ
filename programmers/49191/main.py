# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    win = {i: set() for i in range(1, n+1)}
    lose = {i: set() for i in range(1, n+1)}
    for A, B in results:
        win[A].add(B)
        lose[B].add(A)

    for i in range(1, n+1):
        for loser in win[i]: # i에게 진 loser를 이긴 사람들의 목록에 i를 이긴 사람들의 목록을 추가한다.
            lose[loser].update(lose[i])
        for winner in lose[i]: # i에게 이긴 winner에게 진 사람들의 목록에 i에게 진 사람들의 목록을 추가한다.
            win[winner].update(win[i])

    result = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            result += 1

    return result

print(solution(
    5,
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
), 2)