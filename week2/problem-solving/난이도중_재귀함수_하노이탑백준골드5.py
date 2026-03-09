# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

k = 0#이동회수
arr = []#이동경로 리스트
def tower(no, x, y):
    global k 
    
    if no > 1:
        tower(no - 1, x, 6 - x - y)
        
    arr.append((x, y))  
    k = k+1
    if no > 1:
        tower(no - 1, 6 - x - y, y)


num = int(input())

if num > 20:
    print(2**num - 1)
else:
    tower(num, 1, 3)
    print(k)
    for i in arr:
        print(i[0], i[1])