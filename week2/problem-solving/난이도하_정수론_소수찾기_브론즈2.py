# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
numCount=int(input())
placeholder=0
data=list(map(int, input().split()))
for x in data:
    if x < 2: 
        continue
    error = 0 
    for i in range(2, x):
        if x % i == 0:    
            error += 1    
            break         
    if error == 0:
        placeholder += 1
print (placeholder)