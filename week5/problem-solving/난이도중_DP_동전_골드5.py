# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

T = int(input())   #테스트 케이스 개수 입력받기

for _ in range(T): 
    N = int(input()) #동전가지수
    coins = list(map(int, input().split())) #동전 종류 
    M = int(input())            #금액 M

    dp = [0] * (M + 1)  #배열 선언
    dp[0] = 1

    for coin in coins:
        for j in range(coin, M + 1):
            dp[j] = dp[j] + dp[j - coin]

    print(dp[M])