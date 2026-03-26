# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725


#이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

#입력
#트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

#출력
#입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []

while True:
    try:
        line = input().strip()          # 백준식 입력 개수 안 정해져 있을 때 입력
        if not line:
            break
        preorder.append(int(line))
    except:  
        break

def postorder(start, end):
    if start > end:
        return

    root = preorder[start]

    split = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            split = i
            break

    postorder(start + 1, split - 1)  
    postorder(split, end)            
    print(root)

postorder(0, len(preorder) - 1)