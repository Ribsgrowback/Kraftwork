# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
n=int(input()) #N 값 인풋
ans = 0
board = [0] * n
def solve(row):
    # TODO: 기저 조건 처리
    
    # TODO: 현재 행(row)에서 각 열(col)에 퀸 놓아보기
    for col in range(n):
        if is_possible(row):
            solve(row + 1)

def is_possible(row):
    # TODO: row 이전의 행들과 충돌하는지 체크 (세로, 대각선)
    
    return True


solve(0)
print(ans)