# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
nums = []
numcount = 0
maximum = 0
for cycle in range(9) :
    nums.append(int(input()))
    if maximum < nums[cycle] :
        maximum = nums[cycle]
        numcount = cycle+1

print(maximum)
print(numcount)