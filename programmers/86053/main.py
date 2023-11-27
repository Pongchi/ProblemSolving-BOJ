# https://school.programmers.co.kr/learn/courses/30/lessons/86053

def solution(a, b, g, s, w, t):
    start = 0
    end = (10**9 + 10**9) * 1 * 10**5

    while start <= end:
        mid = (start+end) // 2
        current_gold = 0
        current_silver = 0
        current_both = 0

        for i in range(len(g)):
            can_move_count = mid // (t[i]*2)
            if mid%(t[i]*2) >= t[i]:
                can_move_count += 1
            current_gold += min(g[i], w[i]*can_move_count)
            current_silver += min(s[i], w[i]*can_move_count)
            current_both +=  min(g[i]+s[i], w[i]*can_move_count)

        if current_gold >= a and current_silver >= b and current_both >= a+b:
            end = mid-1
        else:
            start = mid+1

    return start

print(solution(
    10,
    10,
    [100],
    [100],
    [7],
    [10]
), 50)

print(solution(
    90,
    500,
    [70, 70, 0],
    [0, 0, 500],
    [100, 100, 2],
    [4, 8, 1]
), 499)

print(solution(
    0,
    0,
    [0],
    [0],
    [1],
    [1]
), 0)