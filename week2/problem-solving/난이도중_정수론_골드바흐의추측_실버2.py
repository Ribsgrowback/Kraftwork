# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#is_prime() 쓸걸

t = int(input())

for _ in range(t):
    n = int(input())

    a = n // 2
    b = n // 2
 
    while True:
  
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a =a+ 1
        b =b+ 1