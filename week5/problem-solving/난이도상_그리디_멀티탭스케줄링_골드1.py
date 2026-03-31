# 그리디 - 멀티탭 스케줄링 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1700

N, K = map(int, input().split())
schedule = list(map(int, input().split()))

multitap = []
unplug_count = 0

for i in range(K):
    device = schedule[i]
    if device in multitap:
        continue
    if len(multitap) < N:
        multitap.append(device)
        continue

    unplug_count += 1
    willPlug = {}
    for j in range(i + 1, K):
        if schedule[j] in multitap and schedule[j] not in willPlug:
            willPlug[schedule[j]] = j

    unpluged = None
    future = -1
    for d in multitap:
        if d not in willPlug:
            unpluged = d
            break
        elif willPlug[d] > future:
            future = willPlug[d]
            unpluged = d

    multitap.remove(unpluged)
    multitap.append(device)

print(unplug_count)