# '''
# 9
# 7 4 2 0 0 6 0 7 0
# '''
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# print(N)
# print(arr)


#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_v = arr[0]
#     min_v = 1000000
#     for i in range(1, N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#
#         if min_v > arr[i]:
#             min_v = arr[i]
#
#     ans = max_v - min_v
#
#
#     print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}', *arr)
