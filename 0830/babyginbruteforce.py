def is_triple(lst):
    return lst[0] == lst[1] and lst[1] == lst[2]

def is_run(lst):
    return lst[0] == lst[1] -1 and lst[1] == lst[2] - 1

def baby_gin(idx, used, lst):

    # 종료 조건 : 6개 숫자 자리를 다 정해줌(순열완성)
    if idx == 6:

        앞 = [lst[i] for i in used[:3]]
        뒤 = [lst[i] for i in used[3:]]
        if (is_run(앞) or is_triple(앞)) and (is_triple(뒤) or is_run(뒤)):
            print(f'베이비진! {앞} {뒤}')
        return
    
    for i in range(6):
        if i not in used:
            used.append(i)
            baby_gin(idx + 1, used, lst)
            used.pop()

baby_gin(0, [], [1,2,4,7,8,3])
baby_gin(0, [], [6,6,7,7,6,7])
baby_gin(0, [], [0,5,4,0,6,0])
baby_gin(0, [], [1,0,1,1,2,3])