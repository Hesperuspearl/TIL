def funfun(n):
    if n == 0:
        print(f'{n} : 끝')
        return
    else:
        print(n)
        funfun(n-1)
        print(n)

funfun(10)