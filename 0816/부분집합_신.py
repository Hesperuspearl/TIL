numbers = [1, 2, 3, 4, 5]

selected = [0] * 5
# selected[i] == 1 : 내가 i번째 원소를 부분집합에 포함 o
# selected[i] == 0 : 내가 i번째 원소를 부분집합에 포함 x

n = len(numbers)

# 재귀함수로 부분집합 구하기
# i번째 원소를 부분집합에 포함할지 안할지를 결정해준다
# n-1 번째 원소까지 하면 된다.
# n-1 번째 원소까지 완료한 경우 뒤로 돌아와서 내가 이전에 선택했다면
# 선택하지 않고 진행 ==> 반복

def subset(i, n):

    # 0 : 다른 조건(최적화)
    if subsum > x:
        return
    # 1. 종료 조건
    if i == n:
        # n개의 원소에 대한 선택을 끝냈다.(부분집합에 넣던지 안넣던지)
        for j in range(n):
            temp = 0
            if selected[j]:
                print(numbers[j], end = ' ')
        print()
        return
    
    # 2. 재귀호출
    # i번째 원소를 서낵하고 다음 i + 1 번째 원소를 선택하러 가거나
    selected[i] = 1
    subset(i +1, n)
    # i번째 원소를 선택하지 않고 다음 i+1 번째 원소를 서낵하러 가거나
    selected[i] = 0
    subset(i+1, n)

subset(0, n)