# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020


doCount=int(input()) #getting tastecase T

data=[]
for i in range(doCount):
    data.append(int(input())) #getting data[] X testcase T

#소수찾기 섹션
for j in range(2,1):
    