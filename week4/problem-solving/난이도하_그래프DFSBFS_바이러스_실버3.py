# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
#첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
#둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
#이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.


from collections import deque

N=int(input())
linked=int(input())
graph = [[] for _ in range(N+1)] #인접 리스트 방식으로 그래프 표현, N+1은 컴퓨터 번호가 1부터 시작하기 때문

for _ in range(linked):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)
queue = deque()
queue.append(1) #1번 컴퓨터에서 시작
visited[1] = True

infected_count = 0  
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            infected_count += 1

print(infected_count)