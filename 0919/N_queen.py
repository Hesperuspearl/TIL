def backtracing

for j in range(1, row+1):
    # 좌상
    if row-j >=0 and i - j >= 0 and board[row-j][i-j] == 1:
        can_place = Falsebreak

    # 우상