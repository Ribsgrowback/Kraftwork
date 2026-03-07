# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
number = int(input())
for j in range(number):
    data = input().split()

    counter = int(data[0])
    arr = data[1]

    for char in arr:
        if counter > 0 :
            print(char * counter, end='')
    print()