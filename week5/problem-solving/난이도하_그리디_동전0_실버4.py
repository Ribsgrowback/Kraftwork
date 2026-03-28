# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

#첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

#둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
# (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
n,k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input())) 

result = {}
total_coins = 0

for coin in reversed(coins):
    count = k // coin  # 현재 동전으로 거슬러줄 수 있는 개수
    if count > 0:
        result[coin] = count  # 결과에 추가
        total_coins += count  # 총 개수 업데이트
        k = k - (coin *count)  # 남은 금액 업데이트

print(total_coins)