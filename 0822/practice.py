def enq(t):
    global last
    last += 1

    heap[last] = t

    c = last
    p = last // 2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    candidates = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0
    ans = 0

    for i in candidates:
        enq(i)

    while last > 0:
        last //= 2
        ans += heap[last]
    
    print(f'#{tc} {ans}')
