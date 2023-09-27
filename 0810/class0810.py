# def dfs(n, V, adj_m):
#     stack = [] # stack 생성
#     visited = [0] * (V+1) # visited 생성
#     visited[n] = 1 # 시작점 방문 표시
#     print(n) # do[n]
#     while True:
#         for w in range(1, V): # 현재 정점 n에 인접하고 미방문 w 찾기
#             if adj_m[n][w] == 1 and visited[w] == 0:
#                 stack.append(n)    # push(v), v = w
#                 n = w    # do(w)
#                 print(n)
#                 visited[n] = 1    # w 방문 표시 visited.
#                 break    # for w, n에 인접인 w c 찾은 경우
#         else:
#             if stack:    # 스택에 지나온 정점이 남아있으면
#                 n = stack.pop()    # pop해서 다시 다른 w를 찾을 n 준비
#             else:    # 스택이 비어있으면
#                 break     # while True 탐색 끝


# V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
# arr = list(map(int, input().split()))
# adj_m = [[0]*(V+1) for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1

# dfs(1, V)


#신민석 강사님
# 그래프의 형태를 어떤 방법으로 나타내느냐
# 1. 인접행렬 => 2차원 배열
# 1번 정점에서 2번 정점으로 가는 길이 있다
# adj_m[1][2] = 1
# 2번 정점에서 3번 정점으로 가는 길이 없다
# adj_m[2][3] = 0
#     A B C D E F 

# s : 시작 정점 번호
# V : 정점의 개수
# def dfs(s, V):
#     stack = []
#     visited = [0] * V

#     # 시작 정점은 방문했다고 처리
#     visited[s] = 1
#     print(node[s])
#     i  = s

#     # 모든 정점을 방문할때까지 반복
#     while True:
#         # 현재 있는 정점에서 탐색할 수 있는 정점이 있는지 확인
#         # i에서 다른 정점 j 로 갈 수 있는 길이 있는지 어떻게 확인?
#         # 인접행렬 or 인접리스트
#         # adj_m[i][j] == 1 이면 길이 있다.
#         for j in range(V):
#               # 내가 이전에 j번 정점을 방문한 적이 있는지도 확인
#               if adj_m[i][j] == 1 and visited[j] == 0:
#                     # j번째 정점을 방문할 것이기 때문에 이전 정점인 i로 되돌아 오기 위해 i를 스택 추가
#                     stack.append(i)
#                    # j번째 정점에서 하고싶은 일
#                     print(node[j])
#                     # 방문했다고 처리
#                     visited[j] = 1
#                     # 현재 위치를 j로 바꾸고 다음 탐색 시작
#                     i = j
#                     # 멈추고 새로운 i에서의 방문을 다시 시작하기 위해 break
#                     break
#         else:
#             # 내가 i에서 탐색을 해봤는데 더이상 탐색을 할 정점이 없다.
#             # 제일 최근에 방문했던 정점으로 돌아가기
#             if stack:
#                   # stack 안에 원소가 있다. 돌아갈 곳 존재.
#                   # 하나 꺼내서 되돌아가기, i 번 정점부터 탐색 시작
#                   i = stack.pop()
#             else: # 남은 정점 없다. 종료
#                  break
#     # return

# adj_m = [[0, 1, 1, 0, 0, 0, 0],  # A
#          [1, 0, 0, 1, 1, 0, 0],  # B
#          [1, 0, 0, 0, 1, 0, 0],  # C
#          [0, 1, 0, 0, 0, 1, 0],  # D
#          [0, 1, 1, 0, 0, 1, 0],  # E
#          [0, 0, 0, 1, 1, 0, 1],  # F
#          [0, 0, 0, 0, 0, 1, 0]   # G
#          ]

# node = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# N = 7
# dfs(0, N)

# 2. 인접리스트
# adj_l[i] => i번 정점과 연결되어있는 정점의 모음(리스트)
# adj_l[A] = [B, C]

'''
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''
def dfs_1(s, V):
     # 초기화
    visited = [0] * (V+1)
    stack = []

    # 시작정점 방문처리
    # 현재 정점을 i 라고 하자.
    i = s
    visited[i] = 1
    print(i)

    # 모든 정점을 방문할 때까지 반복
    while True:
     # 현재 정점 i에서 갈 수 있는 정점 j 를 찾기
        for j in adj_l[i]: 
        # j는 i와 연결되어있는 정점임
        # j 를 방문한적이 있는지만 확인하고 탐색
            if visited[j] == 0:
                stack.append(i)
                i = j
                visited[j] = 1
                print(i)
                break
        # 현재 정점 i에서 갈 수 있는 정점이 없다
        else:
        # 돌아가기
            if stack:
                i = stack.pop()
            else:
                break
        

V, E = map(int, input().split()) # 간선개수
# 인접 리스트
adj_l = [[] for _ in range(V + 1)] # 0번 인덱스 사용 못함. +1
for i in range(E):
     # 연결이 되려면 연결시작점 s, 연결 종료 e
    s, e = map(int, input().split())
     # 인접행렬
    #  adj_m[s][e] = 1
    #  adj_m[e][s] = 1

    #여기 인접리스트에선
    # adj_l[s] = s 정점에서 갈 수 있는 정점들의 리스트
    adj_l[s].append(e)
    adj_l[e].append(s)



dfs_1(1, V)