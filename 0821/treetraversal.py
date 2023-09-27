N = int(input())
tree = list(map(int, input().split()))

cleft = [0] * (N+1)
cright = [0] * (N+1)

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
        print(t, end= '')
        
        preorder(cleft[t])

        preorder(cright[t])

# 2. 중위순회 inorder L - V - R
def inorder(t):
    if t:
        

# 3. 후위순회 postorder L - R - V

def postorder(t):
    if t:
        postorder(cleft[t])
        
        postorder(cright[t])

        print(t, end = '')

preorder(1)
print()
inorder(1)
print()
postorder(1)
