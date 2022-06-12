# Linear Search

# 원하는 값이 나올 떄까지 맨 앞부터 스캔하며 검색, 정렬되지 않은 배열에서 사용
# O(n) 만큼 소요
# 종료조건은 검색한 키값에 해당하는 원소가 없어 인덱스를 벗어나는 경우
# 혹은 검색한 키값에 해당하는 원소를 찾은 경우

from typing import Any, Sequence
import copy


def linear(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):  # 마지막 인덱스까지 갔으나 원하는 값이 없음
            return 'Not Found'
        if a[i] == key:  # 검색 성공하여 해당 인덱스 반환, key값에 해당하는 원소가 여러개 일 경우 맨 앞에 있는거 반환
            return f'x{i}에 존재'
        i += 1
# for 문을 이용한 선형검색
    # for i, e in enumerate(a):
    #     if key == e:
    #         return i
    # return -1

# While 문에서 보초법 활용
# 마지막 인덱스인가 확인하는 if문의 검사비용을 줄이기 위해 Sequence의 마지막에 찾는 키값을 추가하는 방법


def linear2(a: Sequence, key: Any) -> int:
    x = copy.deepcopy(a)
    x.append(key)

    i = 0
    while True:
        if x[i] == key:
            break
        i += 1
    return -1 if i == len(a) else i

# Sequence의 마지막에 key값을 넣어서 무조건 값을 찾게 되므로 마지막 인덱스인가 확인하는 if문의 검사비용이 없어짐.


# Binary Search
# 이진 검색은 정렬된 배열에서 아주 빠르게 key값을 찾는 방법이다.
# O(log n) 만큼 소요

# 오름차순으로 정렬된
# 하나의 배열에서 원하는 key값을 찾으려 할때 검색범위의 시작을 pl , 중앙을 pc, 끝을 pr 이라 하면
# 맨 처음에는 pl = 0, pr = n-1, pc = (0 + n - 1)//2 로 설정한다.
# 그 후에는 인덱스가 pc인 값이 찾는 값인지 확인하고 아니면 검색 범위를 줄인다.
# 1. 만약 pc에서의 값이 key 값보다 작았다면
# 	검색범위를 pl ~ pc -1 로 축소 -> pl = 0, pr = pc - 1, pc = (pl + pr)//2
# 2. 만약 pc에서의 값이 key 값보다 크다면
# 	검색범위를 pc + 1 ~ pr 로 축소 -> pl = pc + 1, pr = n-1, pc = (pl + pr)//2

# 종료조건은 1. 배열[pc] == key
# 			2. 검색 범위가 더 이상 없는 경우


def bin(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:  # 검색 성공
            return pc
        elif a[pc] < key:  # 검색 범위 축소
            pl = pc + 1
        else: 	# 검색 범위 축소
            pr = pc - 1

        if pl > pr:  # 종료조건2
            break
    return -1


if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] = :'))

    key = int(input('key :'))

    # print(linear(x, key))
    print(bin(x, key))
