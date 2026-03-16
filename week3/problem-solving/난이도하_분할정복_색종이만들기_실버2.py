# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

#arr = [list(map(int, input().split())) for _ in range(N)]

def solve(x, y, size):
    color = arr[x][y]
    global white, blue
    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] != color:
                half = size // 2
                solve(x, y, half)
                solve(x, y+half, half)
                solve(x+half, y, half)
                solve(x+half, y+half, half)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))
white=0/4
blue=0
solve(0, 0, N)

print(white)
print(blue)