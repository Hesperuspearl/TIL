T = int(input())
for tc in range(1, T+1):
    D, A, B = list(map(int, input().split()))

    # 소수 빈 리스트 생성
    prime_num = []
    # M부터 N까지 for문을 회전하면서 하나씩 수가 소수인지 확인
    for i in range(A, B+1):
        condition = True
        # 1은 소수가 아님
        if i == 1 : continue
        # 2이상 부터 이중 for문으로 2부터 해당 수까지 반복문을 돌려 0으로 나누어떨어지는지 확인
        # 나누어 떨어지면 소수가 아니므로 바로 break
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                condition = False
                break
        # 이중 for문을 다 돌고 나오면, 0으로 나누어떨어지는 수가 없다는 의미
        # 즉 condition(조건)이 True이므로 소수리스트에 추가
        if condition:
            prime_num.append(i)
    # 리스트 unpacking & 구분자로 줄바꿈을 넣고 출력
    print(prime_num)