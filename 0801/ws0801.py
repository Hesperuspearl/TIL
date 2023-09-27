
for i : 1 -> 4
    counts[i] += counts[i-1]

for j: N-1 -> 0


    # BABY GIN

num = 456789 #Baby Gin 확인할 6자리 수
c = [0] * 12 #6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트. 12개하는 이유는 에러 없앰?

for i in range(6):
    c[num % 10] += 1
    num //= 10
