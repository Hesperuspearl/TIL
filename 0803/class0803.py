부분집합의 수

2의 n승개


def print_subset(bit, arr, n):
    total = 0 #부분집합의 합
    for i in range(n):
        if bit[i]:
            print(arr[i], end = '')
            total += arr[i]
    print(bit, total)

arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit, arr, 4)




#비트연산자
비트 연산자
&
|
<<
>>

<<연산자
1 << n : 2의 n승 즉, 원소가 n개인 경우의 모든 부분집합의 수를 의미한다.

&연산자
i&(1<<j) : i의 j번째 비트가 1인지 아닌지를 검사한다.

arr = [3, 6, 7, 1, 5, 4]

n = len(arr) #n : 집합의 원소의 개수
#arr의 부분집합의 개수 2^6 == 1 << 6 == 1 * 2^6
# 3 << 4 == 3*2^4

#모든 부분집합을 검사

for i in range(1<<n): #부분 집합의 개수
    # i번째 부분집합을 검사하겠다
    # i번째 부분집합이 n개의 원소 중에 j번째를 원소를 포함하는지          #비트 이진수
    for j in range(n): #원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번 비트가 1인경우  #if i & (1<<j) ==1 이라고 하면 안됨! 왜? 100 이런식으로도 나옴.
            print(arr[j], end=',')  # j번 원소 출력
    print()
print()


#이진검색(Binary Search)
자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

def binarySearch(a, N, key)
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:  # 검색 성공
            return true
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return false             #검색 실패


#선택 정렬(Selection sort), Bubble sort와 구별!
def SelectionSort(a, N)
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]   #if i != dlk

#셀렉션 알고리즘
k번째로 작은 원소를 찾는 알고리즘
def select(arr, k):
    for i in range(0, k):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr[k-1]
