# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

left = list(input())
right = []

cmdNum = int(input())

for _ in range(cmdNum):
    cmd = input().split()

    if cmd[0]=="L":
        if left:
            right.append(left.pop())

    elif cmd[0]=="D":
        if right:
            left.append(right.pop())

    elif cmd[0]=="B":
        if left:
            left.pop()

    elif cmd[0]=="P":
        left.append(cmd[1])

print("".join(left+right[::-1]))