# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))               #입력부분, meetings에 시작시간 종료시간 저장

def sort_key(x):
    return (x[1], x[0])
meetings.sort(key=sort_key)

count = 0
last_end = 0
for start, end in meetings:
    if start >= last_end:
        count= count + 1
        last_end = end

print(count)