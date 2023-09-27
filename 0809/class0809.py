# 스택 사용 (파이썬의 메소드)

stack = []

def py_push(item):
    stack.append(item)


# stack.append(item) # push
#
# if len(stack) > 0:
#     stack.pop() # pop


def py_pop():
    if len(stack) == 0:
        # 언더플로우!
        return

    else:
        return stack.pop()

for i in range(10):
    py_push(i)

print(stack)

for i in range(10):
    print(py_pop(), end = '')

print()
print(stack)


# 스택 상용(인덱스)

top = -1 # 원소를 마지막으로 삽입한 위치
size = 10
stack = [0] * size

def my_push(item):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

def my_pop():
    global top
    if top == -1:
        print('underflow!')
        return
    else:
         top -= 1           # top -1 먼저하고 +1 하는 이유는 return문 먼저 만나면 거기서 종료.
         return stack[top+1]

def peek():
    # top이 -1 이면 원소가 없다
    if top > -1:
        return stack[top]

for i in range(10):
    my_push(i)
print(stack)

for i in range(10):
    print(my_pop(), end = '')

print()
print(stack)

# 인덱스로 하면 직접 삭제안함 결과에서 보듯이.
print(stack, top)
my_push(100)
print(stack)
# 100으로 바뀜. 그냥 더미 데이터, 흔적이라고 보면 됨.


# 괄호 조사 알고리즘
T = int(input())

for tc in range(1, T+1):
    row = input() # 괄호의 짝이 맞는지 검사할 문자열

    stack = []

    answer = 1 # 1이면 제대로, 0이면 제대로 x

    # 괄호 검사
    # row 에서 한 글자씩 떼어 와서 검사
    # 떼어낸 한 글자가 만약 여는 괄호다 ? => 스택에 삽입
    # 떼어낸 글자가 닫는 괄호다 => 스택에서 하나 꺼내온 다음에 짝이 맞는지 검사
    # 꺼내오기 전에 스택이 비어있나 확인, 비어있으면 오류!
    # 모든 글자 검사가 끝난 후에 스택이 비어있지 않으면 오류!

    print('#{tc} {answer}')



