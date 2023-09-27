import time
from collections import deque

N = 100000

start = time.time()

q1 = []

for i in range(N):
    q1.append(i)

for i in range(N):
    q1.pop(0)

end = time.time()

print(f'리스트 구현 큐 걸린시간 : {end-start:.5f}')




front  = rear = -1
q3 = [0] * N

start = time.time()

for i in range(N):
    rear += 1
    q3[rear] = i

for i in range(N):
    front += 1

end = time.time()

print(f'선형 큐 걸린 시간 : {end - start:.5f}')
