T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    letters = []
    # 각 줄 길이 최대 15로 설정
    for i in range(15):
        for j in range(5):
            # try 명령 실행, 오류 시 pass
            try: letters.append(arr[j][i])
            except IndexError:
                pass
    result = ''.join(letters)
    print(f'#{tc} {result}')

