# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
import itertools
n = int(input())

data = list(map(int, input().split()))
all_cases = list(itertools.permutations(data, n))

max_result = 0

for case in all_cases:
    current_sum = 0
    for i in range(n - 1):
        current_sum =current_sum + abs(case[i] - case[i+1])

    if current_sum > max_result:
        max_result = current_sum

print(max_result)