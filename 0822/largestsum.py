arr = [10, 6, 4, 5, 1, 3, 2, 9, 7, 8] # 힙에다가 넣을 것

# 최대 힙
heap = [0] * 11
# 마지막에 넣은 원소 위치를 비교할
last = 0

# 삽입 연산
def enq(item):
    global last
    last += 1 # 마지막 위치에 원소 추가
    heap[last] = item

    # 원소를 추가하고나서 부모노드 > 자식노드 이 조건을 만족하도록 해야 한다.
    # 현재 위치를 자식 노드로 생각
    # 부모노드의 위치를 계산
    c = last
    p = c // 2
    # 부모노드가 존재하고, 자식노드가 부모노드보다 작을 때까지 위치를 바꾼다.
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 그 위의 부모랑도 비교
        # 자식과 부모의 위치를 그 위로 바꾸고 계속 비교 이어나가기
        c = p
        p = c // 2

for i in range(10):
    enq(arr[i])

print(heap)
