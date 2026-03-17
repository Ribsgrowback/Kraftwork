# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = []   # (인덱스, 높이)
answer = []

for i in range(N):
    h = heights[i]

    while stack and stack[-1][1] < h:
        stack.pop()

    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0])

    stack.append((i + 1, h))  # 문제는 1번 탑부터 시작

print(*answer)