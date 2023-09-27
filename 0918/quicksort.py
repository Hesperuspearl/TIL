def partition(A, l, r):
    p = A[l]

    i, j = l, r


    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        
        while i <= j and A[j] >= p:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]


    A[l], A[j] = A[j], A[l]

    print("Swap end")
    print(f'p: {A[j]}')
    print(A)
    print('========')

    return j

def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s - 1)
        quickSort(A, s + 1, r)

l1 = [11, 45, 23, 81, 28, 34]
l2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
l3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

N = len(l1)
quickSort(l1, 0, N - 1)
print(l1)