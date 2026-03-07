# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

testcaseNumC = (int(input())) # 테스트케이스 개수 C mock 입력값 5
total_score = 0

for N in range(testcaseNumC):
    data = list(map(int, input().split())) #data에 배열로 저장?
    n = data[0]
    scores = data[1:]

    total_score = sum(scores) 
    avg = total_score / n
    

    count = 0    #평균 넘는 학생 수 세기
    for s in scores:
        if s > avg:
            count += 1
            
  
    ratio = (count / n) * 100   #비율 계산 및 소수점 셋째 자리 출력
    print(f"{ratio:.3f}%")