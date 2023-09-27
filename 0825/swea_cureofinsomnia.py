def counting(k, N):     # 0~9까지의 숫자가 모두 나왔을 때가 몇번 양인지 세는 함수
    # N의 값을 문자화하여 num list에 하나씩 저장
    for i in str(k * N):
        num.append(i)
    # set화하여 중복을 없앤 후 원소개수(길이)가 10이 아닐 경우,
    # k값에 1을 더하고, 다시 counting 함수 수행
    if len(set(num)) != 10:
        k += 1
        counting(k, N)
    # set(num)의 길이가 10이 되면, 0~9까지 다 들어갔다는 뜻
    else:
        print(f'#{tc} {k * N}')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = []
    # k 초기값
    k = 1
    counting(k, N)
    # print(num)
    # print(set(num))

