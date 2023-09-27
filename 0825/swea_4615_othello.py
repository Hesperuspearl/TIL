def f(i, j, bw, N):
    board[i][j] = bw
    for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i+di, i+dj

        while 0 <= ni < N and 0<=nj<N and board[ni][nj] == op[bw]:
            tmp.append((ni, nj))
            ni, nj = ni + di, nj + dj
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = bw


B = 1
W = 2
op = [0, 2, 1]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]

    # 중심부 4개의 돌 배지
    board[N//2-1][N//2-1] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W
    for col, row, bw in play:
        f(row-1, col-1, bw, N)
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1
    print(f'#{tc} {bcnt} {wcnt}')

