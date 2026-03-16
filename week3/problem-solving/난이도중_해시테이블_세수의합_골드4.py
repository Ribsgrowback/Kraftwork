# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

def solver(arr):
    arr.sort()

    two_sum = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            two_sum.add(arr[i] + arr[j])

    for i in range(len(arr)-1, -1, -1):
        d = arr[i]
        for j in range(i+1):
            z = arr[j]
            if d-z in two_sum:
                return d


N = int(input())
arr=[]
for u in range(N):
    arr.append(int(input()))

print(solver(arr))