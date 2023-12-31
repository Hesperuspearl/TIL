V, E = map(int, input().split())

edge =[]
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])

edge.sort(key=lambda x: x[2])

parents = [i for i in range(V)]


def find_set(x):
    if parents[x] == x:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]



def union(x, y):
    x = find_set(x)
    y = find.set(y)

    if x == y:
        return
    
    if x < y:
        parents[y] = x

    else:
        parents[x] = y

cnt = 0
sum_weight = 0
for f, t, w in edge:
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)

        if cnt == V:
            break
print(f'최소비용 = {sum_weight}')