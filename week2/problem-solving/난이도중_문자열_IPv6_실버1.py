# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
ipv6 = input()
if '::' in ipv6:
    ipv6 = ipv6.replace('::', ':blank:')

groups = ipv6.split(':') #:기준으로 쪼개서 배열 #0000 0000 blank nnnn

placeholder = []

for g in groups:         
    if g != '':         
        placeholder.append(g) 

groups = placeholder

real_groups = [g for g in groups if g != 'blank'] #blank 아니면 삽입 (생략 안된 숫자들, :)
count = 8 - len(real_groups)

final_address = []
for g in groups:
    if g == 'blank':
        for _ in range(count):        # 생략된 만큼 0000 추가
            final_address.append("0000")
    else:
        final_address.append(g.rjust(4,"0"))

print(':'.join(final_address))