

# 문제 유형
# 1. 특정 지점 -> 도착 지점까지 최단 거리: 다익스트라
# 2. 가중치에 음수가 포함되어 있네? : 밸만포드
# 3. 여러 지점 -> 여러 지점까지의 최단 거리 : 플로이드-워샬
     # -> 여러 지점 모두 다익스트라 돌리기 -> 시간 복잡도 계산 잘해야함



import heapq

n, m = map(int, input().xplit())

graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

INF = int(1e9)
distance = [INF] * n

def dijkstra(start):

    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue
                
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)



