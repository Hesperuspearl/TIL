# #1861 정사각형 방

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     max_cnt = 0
#     max_start = 0
#     for p in range(N):
#         for q in range(N):
#             i, j = p, q
#             cnt = 1
#             start = arr[i][j]

#             while True:
#                 for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:




#     if max_cnt < cnt:
#         max_nct = cnt

#     cnt == 

# else:
#     breakkkkkke


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ones = [0] * (N *N+1)
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0,-1],[-1,0]]:
                ni, nj = i + di, j + dj
                if 0<=ni<N and 0<=nj<N and arr[i][j]+1 == arr[ni][nj]:
                    ones[arr[i][j]] = 1
    max_cnt = 0
    max_start = 0
    c = 0
    for k in range(N*N, 0, -1):
        if ones[k]:
            c += 1
            if max_cnt<c:
                max_cnt = c
                max_start = k
            elif max_cnt == c:
                max_start = k
        else:
            c = 0
    print(f'#{tc} {max_start} {max_cnt+1}')

