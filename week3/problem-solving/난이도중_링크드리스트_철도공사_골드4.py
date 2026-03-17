# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

# 음

# 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
station = list(map(int, input().split()))

next={}
prev={}

for i in range(N):
    next[station[i]]=station[(i+1) % N]
    prev[station[i]]=station[(i-1) % N]

for _ in range(M):
    cmd=input().split()

    if cmd[0]=="BN":
        i=int(cmd[1])
        j=int(cmd[2])

        print(next[i])

        j_next = next[i]
        next[i]=j
        prev[j]=i
        next[j]=j_next
        prev[j_next]=j

    elif cmd[0] == "BP":
        i=int(cmd[1])
        j=int(cmd[2])

        print(prev[i])

        i_prev = prev[i]
        next[i_prev] = j
        prev[j] = i_prev
        next[j] = i
        prev[i] = j

    elif cmd[0] == "CN":
        i = int(cmd[1])

        target = next[i]
        print(target)

        next[i] = next[target]
        prev[next[target]] = i

    elif cmd[0] == "CP":
        i = int(cmd[1])

        target = prev[i]
        print(target)

        prev[i] = prev[target]
        next[prev[target]] = i