def solution(n, money):
    dp = [0] * (n + 1)

    for coin in money:
        dp[coin] += 1
        for i in range(coin, n+1):
            dp[i] += dp[i - coin]

    return dp[n] % 1000000007

print(solution(
    5,
    [5, 2, 1]
), 4)