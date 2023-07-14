
#컴퓨터가 내는거 random
#누가 이겼는지 판별 후 승자 출력, 게임 결과도 출력, ex내가 가위를 내고 컴퓨터가 바위를 내서 패배하였습니다.



user = input()

print(user)


import random
l = ['가위', '바위', '보']
com = random.choice(l)
print(com)

R = None
if (user == '가위' and com == '가위') or (user == '바위' and com == '바위') or (user == '보' and com == '보'):
    R = '무승부'
elif (user == '가위' and com == '보') or (user == '바위' and com == '가위') or (user == '보' and com == '바위'):
    R = '승리'
elif (user == '가위' and com == '바위') or (user == '바위' and com == '보') or (user == '보' and com == '가위'):
    R = '패배'

print(f'나는 {user}를 내고 컴퓨터가 {com}을 내서 {R}!')



