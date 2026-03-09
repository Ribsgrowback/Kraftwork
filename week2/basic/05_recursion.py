

def factorial(n):
    if n <= 1:
        return 1
    return n* factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 테스트 케이스
if __name__ == "__main__":
    # 팩토리얼 테스트
    print("=== 팩토리얼 계산 ===")
    for i in range(6):
        result = factorial(i)
        print(f"{i}! = {result}")
    print()
    
    # 피보나치 테스트
    print("=== 피보나치 수열 ===")
    for i in range(10):
        result = fibonacci(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 추가 테스트
    print("=== 추가 테스트 ===")
    print(f"10! = {factorial(10)}")
    print(f"fib(15) = {fibonacci(15)}")