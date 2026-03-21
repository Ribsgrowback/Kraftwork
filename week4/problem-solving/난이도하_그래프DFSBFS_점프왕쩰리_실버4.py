# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# N=int(input())
# # fieldmap=[]
# # for i in range(N):
# #     fieldmap[i].append(list(map(int, input().split())))
# fieldmap = []
# for i in range(N):
#     fieldmap.append(list(map(int, input().split())))

# for j in range(N):
#     for k in range(N):
#         if fieldmap[j][k] != -1:
#             if fieldmap[j][k] == -1:
#                 print("HaruHaru")
#                 break
#             else:
#                 jump = fieldmap[j][k]
#                 j += jump
#                 k += jump
from collections import deque

N = int(input())
fieldmap = [list(map(int, input().split())) for _ in range(N)] #이중배열 맵 입력

visited = [[False] * N for _ in range(N)] #방문 여부를 저장하는 2차원 리스트, 초기값은 모두 False로 설정 (배열을 하나더)
queue = deque()
queue.append((0, 0))
visited[0][0] = True

while queue:
    x, y = queue.popleft()

    if fieldmap[x][y] == -1:
        print("HaruHaru")
        break

    jump = fieldmap[x][y]

    nx = x + jump
    ny = y
    if 0 <= nx < N and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx, ny))

    nx = x
    ny = y + jump
    if 0 <= ny < N and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx, ny))

else:
    print("Hing")
