# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

while True:
    try:
        N, K = map(int, input().split())
        items = []
        for _ in range(N):
            weight, value = map(int, input().split())
            items.append((weight, value)) #입력받기, items에 무게와 가치 저장


        dp = [[0] * (K + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            weight, value = items[i - 1]
            for j in range(K + 1):
                if weight > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

        print(dp[N][K])
    except EOFError:
        break

