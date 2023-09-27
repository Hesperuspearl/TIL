p = [i for i in range(V)]



def find_set(x):
    while x != p[x]:
        x = p[x]

    return x

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        p[y] = x

    else:
        p[x] = y

V, E = map(int, input().split())
edge = []

for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append((w, s, e))


edge.sort()
p = 

cnt = 0
total = 0

for w, s, e in edge:
    if find_set(s) != find_set(e):
        cnt += 1
        