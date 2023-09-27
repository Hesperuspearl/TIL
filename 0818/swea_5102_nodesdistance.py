def bfs(S, G, V):
    visited = [0] * (V+1)
    q = []
    # q에 시작점 S 삽입
    q.append(S)
    # visited S 부분 1로 변경
    visited[S] = 1
    # q가 빌 때까지 수행
    while q:
        t = q.pop(0)
        # 정점 t와 연결된 i 탐색
        for i in routes[t]:
            # visited, 0이라면, 즉 방문하지 않은 상태일 경우, 인큐
            if not visited[i]:
                q.append(i)
                # 목표지점까지의 간선 횟수를 누적으로 구하기 위해 visited[t]에 + 1
                visited[i] = visited[t] + 1
        if visited[G] > 0:
            # 종점까지 도착 후, visited 숫자에서 -1 을 하여 간선 횟수 구함
            return visited[G] - 1

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    routes = [[] for _ in range(V + 1)]
    
    for i in range(E):      # routes에 인덱스 숫자의 인접 숫자들 입력
        start, to = map(int, input().split())
        routes[start].append(to)
        routes[to].append(start)
    
    S, G = map(int, input().split())    # 출발점, 도착점

    ans = bfs(S, G, V)

    print(f'#{tc} {ans}')

