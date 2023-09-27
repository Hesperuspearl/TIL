N = int(input())
tree = list(map(int, input().split()))

# 인덱스가 부모노드의 번호
cleft = [0] * (N + 1)
cright = [0] * (N + 1)

for i in range(N - 1):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c


# 1. 전위순회 preorder V - L - R
def preorder(t):
    if t:
        # t에서 방문처리
        print(t, end=" ")
        # 왼쪽
        preorder(cleft[t])
        # 오른쪽
        preorder(cright[t])
preorder(1)