A = [69, 10, 30, 2, 16, 8, 31, 22]


def merge(left, right):
    result = []

    if left[0] <= right[0]:
        result.append(left[0])

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))


    return result


def mergeSort(lst):
    m = len(lst)

    if m == 1:
        return lst
    
    mid = m // 2

    left, right = lst[:mid], lst[mid:] # 얕은 복사
    
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

print(mergeSort(A))