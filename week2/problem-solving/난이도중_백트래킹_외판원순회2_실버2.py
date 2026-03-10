# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
import sys

data = sys.stdin.readline

def dfs(now, count, cost):
    global min_cost

    if cost >= min_cost: #현재코스트가 최저 코스트를 넘치면 의미 없으므로 리턴
        return

    if count == N:
        if W[now][0] != 0:
            min_cost = min(min_cost, cost + W[now][0]) #출발지로 돌아우는 루트 없으면 리턴
        return

    for i in range(N): #탐색
        if not visited[i] and W[now][i] != 0:
            visited[i] = True  # 방문 처리
            dfs(i, count + 1, cost + W[now][i]) #재귀
            visited[i] = False # 백트랙

N = int(data())
W = [list(map(int, data().split())) for _ in range(N)]

visited = [False] * N                                           
min_cost = sys.maxsize 

visited[0] = True
dfs(0, 1, 0)

print(min_cost)