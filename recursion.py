# 유클리드 호제법

from FixedStack import FixedStack
from numpy import rec


def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# 재귀함수

def recur(n: int) -> int:
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)


# 꼬리 재귀없애기
# recur()의 마지막에 있는 recur(n - 2) 는 결국 인수로 n - 2 를 전달하고 recur()을 호출하는 것
# 따라서 이 호출을 다음과 같이 바꿀 수 있다.
# n의 값을 n - 2 로 업데이트하고 함수의 시작지점으로 돌아간다

def recur_without_tail(n: int) -> int:
    while n > 0:
        recur_without_tail(n - 1)
        print(n)
        n = n - 2


# recur_without_tail(4)

# 재귀 없애기
# recur(n - 1)의 경우 꼬리 재귀처럼 n 값을 n - 1 로 업데이트한 후 시작지점으로 돌아갈 수 없다.
# 왜냐면 처음들어온 n값을 recur(n - 1)이 끝날때까지 저장해뒀다가 끝나면 출력해줘야 하는데
# n값을 위에서 업데이트 해버리면 처음에 들어온 n값을 잃어버리게 되어서 문제가 생긴다.

# 위의 문제를 스택으로 해결할 수 있다.


def recur_stack(n: int) -> int:
    # 재귀를 제거한 recur함수
    s = FixedStack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break

# 스택프레임에 함수가 쌓이는 것과 같이 n이 스택에 쌓이는 듯

# 하노이의 탑
# 시작기둥, 중간기둥, 목표기둥 이 있을 때
# 원반들을 그룹핑해보자. 맨 아래에 있는 원반을 제외한 나머지 원반을 하나로 보면
# 결국 원반 그룹을 중간기둥에 둔 후, 맨 아래원반을 목표기둥으로 이동시키고, 위의 원반 그룹을 그 위로 이동시키면 된다.
# 즉, 한번에 맨


def move(num: int, x: int, y: int) -> None:  # 원반의 수, 시작기둥번호, 목표기둥번호
    # 원반 num개를 x에서 y로 옮긴다.
    if num > 1:
        move(num - 1, x, 6 - x - y)  # 맨 아래원반을 제외한 나머지를 중간기둥(6 - x - y)으로 옮겨라
    
    print(f'원반 [{num}]을 {x}기둥에서 {y}기둥으로 옮깁니다.') # 맨 아래원반을 목표지점으로 이동
    
    if num > 1:
        move(num - 1, 6 - x - y, y) # 원반 그룹을 중간 기둥에서 목표기둥으로 옮겨라.

# move(3, 1, 3)


# 8퀸 문제
# 8 * 8의 체스판에 8개의 퀸을 서로 공격하지 못하게 배치하는 경우의 수를 찾는 문제
# 퀸은 8가지 방향으로 공격할 수 있다. -> 수평방향, 수직방향, 대각방향
# 만약에 그냥 무작위로 8칸을 뽑아서 조건에 맞는지 확인하려하면 너무나도 많은 경우를 계산해야하기에 불가능.
# 조건중 한가지만 생각해보자.

# 1. 각 열에 퀸을 1개만 배치해야함 -> 수직방향 조건
# 위 조건만으로 경우의 수는 8^8으로 줄어듬
# 2. 각 행에 퀸을 1개만 배치해야함 -> 수평방향 조건
# 2번 조건까지 생각하면 조합의 수가 상당히 줄겠지만, 두가지 조건을 만족하는 조합을 만드는 알고리즘 생각하기 쉽지않음.

# 먼저 1번 조건에 맞는 알고리즘만 생각해보자.
# 1. 각 열에 퀸을 1개만 배치해서 나올 수 있는 모든 조합 구하기

pos = [0] * 8 # 배열 pos는 퀸을 배치를 나타낸다. -> pos의 0~7의 인덱스는 각열을 의미하고 원소의 값은 행의 인덱스를 의미.

def set(i: int) -> None:
    # i열에 퀸을 배치
    for j in range(8):
        pos[i] = j # i번째 열, j번째 행에 퀸을 배치.
        
        if i == 7: # 모든 열에 퀸 배치함.
            put() 
        else:
            set(i + 1) # 다음 열에 퀸 배치

def put() -> None:
    # 각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

# set(0)

# 위의 방법으로 1번 조건에 맞는 모든 조합은 구할 수 있다.
# 이제 다음 조건인 각 행에 퀸 하나만 배치할 수 있다. 를 적용하자.
# 행을 나타내는 배열인 flag를 이용해서 특정 행에 이미 퀸이 있는지 확인할 때 이용하자.

flag = [False] * 8 # 인덱스는 각 행을 의미 / True면 퀸 존재, False면 퀸 없음


def set2(i: int) -> None:
    # i열에 퀸을 배치
    for j in range(8):
        if not flag[j]:
            pos[i] = j
            if i == 7:
                put2()
            else:
                flag[j] = True
                set2(i + 1)
                flag[j] = False # 퀸의 배치를 모두 완료하고 왔을 때, 다시 초기화 하는 것.

def put2() -> None:
    # 각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


# set2(0)

# flag 배열을 이용해 각 행에 이미 퀸이 있는지 없는지 확인한 후 없으면 배치하도록 해서 조건2 달성

# 이제 3번째 조건인 대각선방향을 고려해보자.

flag_b = [False] * 15 # 기울기가 양수인 대각선 총 15개
flag_c = [False] * 15 # 기울기가 음수인 대각선 총 15개 -> 8 * 8 그리드를 그려보고 대각선을 그어보면 알 수 있다.

def set3(i: int) -> None:
    # i열에 퀸을 배치
    for j in range(8):
        if (not flag[j] 
            and not flag_b[i + j]  # 기울기가 양수인 대각선이 False이고
            and not flag_c[i - j + 7]): # 기울기가 음수인 대각선도 False이어야 한다. -> 그리드를 그려보고 대각선의 인덱스 값을 구해보면 i + j , i - j + 7 이 값이 나온다
            pos[i] = j
            if i == 7:
                put4()
            else:
                flag[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set3(i + 1)
                flag[j] = flag_b[i + j] = flag_c[i - j + 7] = False

def put3() -> None:
    # 각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def put4() -> None:
    for i in range(8):
        for j in range(8):
            print('■' if pos[j] == i else '□', end='')
        print()
        
    print()

set3(0)