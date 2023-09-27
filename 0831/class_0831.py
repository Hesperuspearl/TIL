 combination 1

def ncr(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = a[n-1]    # a[n-1] 조합에 포함시키는 경우
        ncr(n-1, r-1)
        ncr(n-1, r)     # a[n-1]을 포함시키지 않는 경우

N = 5
R = 3
a = [1, 2, 3, 4, 5]
tr = [0] * R
ncr(N, R)

# conbination 2

def ncr(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = a[n-1]    # a[n-1] 조합에 포함시키는 경우
        ncr(n-1, r-1)
        ncr(n-1, r)     # a[n-1]을 



if nCr(n, r s):
if  r
A = [1, 2, 3, ,4, 5]
N = len(A)
R = 3
comb = [0] * R
nCr(N, R, 00)


# 부분집합 

def subset(i, N, s):
    if i ==N:
        # for j in range(N):
        #     if bit[j]:
        #         s += arr[j]
        if s == 0:
            for j in range(N):
                if bit[j]:
                    print(arr[j], end = '')
            print()
    else:
        
        subset(i+1, N, s+arr[i])
       
        subset(i+1, N, s)
    return


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N