di = [0, 1]
dj = [1, 0, -1, 0]



N = int(input())
arr = [List(map(int, input().split())) for _ in range(N)]

max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                s += arr[ni][nj]

        if max_v < s:





#전치
