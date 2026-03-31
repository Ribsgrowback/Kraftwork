# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

T = int(input())
for _ in range(T):
    N = int(input())
    applicants = []
    for _ in range(N):
        rank1, rank2 = map(int, input().split())
        applicants.append((rank1, rank2)) 

    applicants.sort(key=lambda x: x[0])

    count = 1
    best_rank2 = applicants[0][1] 
    for i in range(1, N):
        if applicants[i][1] < best_rank2: 
            count += 1
            best_rank2 = applicants[i][1] 

    print(count)