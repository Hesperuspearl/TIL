가위 = 1
바위 = 2
보 = 3




def tournament(i, j): # j는 N
    # 종료조건
    if i == j:
        return i
    # 재귀호출
    else:
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2 + 1, j)

        # 왼쪽과 오른쪽 중에서 승자를 골라서 return
        # cards[left]
        # cards[right]
        return match(left, right)

def match(left, right):
    if cards[left] - cards[right] == -1 or cards[left] - cards[right] == 2:
        return right
    else:
        return left


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    print(f'#{tc} {tournament(1, N)}')