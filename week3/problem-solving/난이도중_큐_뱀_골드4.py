# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
from collections import deque

N = int(input())
field = [[0] * N for _ in range(N)]

apple_num = int(input())
for _ in range(apple_num):
    x, y = map(int, input().split())
    field[x - 1][y - 1] = 1

cmd_num = int(input())
cmd = {}
for _ in range(cmd_num):
    t, d = input().split()
    cmd[int(t)] = d

snake = deque()
snake.append((0, 0))

visited = [[False] * N for _ in range(N)]
visited[0][0] = True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not (0 <= nx < N and 0 <= ny < N):
        break
    if visited[nx][ny]:
        break

    snake.append((nx, ny))
    visited[nx][ny] = True

    if field[nx][ny] == 1:
        field[nx][ny] = 0
    else:
        tx, ty = snake.popleft()
        visited[tx][ty] = False

    x, y = nx, ny

    if time in cmd:
        if cmd[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)