numbers = [1, 2, 3, 4, 5]

n = len(numbers)
# i번째 원소의 자리를 바꿔 가면서 순열 생성
# 자리를 바꿀 수 있는 경우의 수

def  perm1(i):
    if i == n:
        print(numbers)
        return
    # 재귀 호출
     # 현재위치 i에서 다른위치 j에 있는 숫자와 자리를 바꾼다.
     # i를 선택할 때는 중복을 방지하기 위해 i보다 뒤에 있는 원소만 선
    for j in range(a+)]:
        numbers[i] , numbers[i+1]o    

    perm(1)

    numbers = [1, 2, 3, 4, 5]

    # 순열의 i 번째 자리를 누구로 할 것인가 직접사ㅓ택
    # i 번쨰 자리를 누구로 기억해

def perm2:
if i == n:
    return
for j in range(n):
    if numbers j not in seleced:
        selected[i] = numbers[j]
        perm2(i+1, selected)
        selected[i] = 0

perm2(0, [0] * 5)

