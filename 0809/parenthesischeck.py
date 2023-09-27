# 괄호 조사 알고리즘
T = int(input())

for tc in range(1, T+1):
    row = input() # 괄호의 짝이 맞는지 검사할 문자열

    stack = []

    answer = 1 # 1이면 제대로, 0이면 제대로 x
    for c in row:
        if c == '(':
            stack.append(c)

        if c == ')':
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()
            if not(b == '(' and c == ')'):
                answer = 0
                break
    if len(stack) > 0:
        answer = 0



    # row 에서 한 글자씩 떼어 와서 검사
    # 떼어낸 한 글자가 만약 여는 괄호다 ? => 스택에 삽입
    # 떼어낸 글자가 닫는 괄호다 => 스택에서 하나 꺼내온 다음에 짝이 맞는지 검사
    # 꺼내오기 전에 스택이 비어있나 확인, 비어있으면 오류!
    # 모든 글자 검사가 끝난 후에 스택이 비어있지 않으면 오류!

    print(f'#{tc} {answer}')

    # 4
    # ( )()((( )))
    # ((( )((((( )()((( )())((( ))))))
    #        ())
    #       (()