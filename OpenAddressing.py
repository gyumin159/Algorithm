# 오픈 주소법은 해시값에 해당하는 버킷에 이미 다른 원소가 있어서 생기는 충돌을
# 재해시 하면서 해결한다.
# 예를 들어보면 우리의 해시함수는 해시테이블의 크기로 나눠서 나온 나머지를 반환한다.
# 테이블의 크기가 13인 상태에서 키가 18인 원소를 추가하려고 할 때 만약 이미 키가 5인 원소가 이미 있다면
# 오픈 주소법에서는 키 값에 변화를 준 후 다시 해시값을 구한다. -> (키값 += 1 후 다시 해시값 추출)같은 방법으로
# -> 선형 탐사법 이라고도 한다.

# 재해시 때문에 생기는 문제가 있는데
# 바로 원소의 삭제, 검색시 선형 탐사법을 통해 들어간 원소는 기존의 해시값에 맞는 버킷에 들어가지 않고 다른 버킷에 들어가 있다는 것이다.
# 따라서 각 버킷에 다음과 같은 속성을 부여한다
# 데이터가 저장되어 있음, 비어있음, 삭제 완료

from __future__ import annotations
from enum import Enum
import hashlib
import re
from typing import Any, Type


class Status(Enum):  # 버킷의 속성
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    # 해시를 구성하는 버킷
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat  # 속성

    def set(self, key: Any, value: Any, stat: Status) -> None:  # 모든 필드에 값을 설정
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        # 속성 설정
        self.stat = stat


class OpenHash:
    # 오픈 해시법으로 구현하는 해시 클래스

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        # 재해시한 해시값 반환
        return (self.hash_value(key) + 1) % self.capacity
    
    def search_node(self, key: Any) -> Any:
        # 키가 동일한 버킷을 검색
        hash = self.hash_value(key)
        p = self.table[hash]
        
        for _ in range(self.capacity): # 모든 버킷을 돌아볼 수 있으니까 테이블의 크기만큼 반복
            if p.stat == Status.EMPTY: # 해당 버킷이 비어있다면 해당 값이 없다는 것.
                break
            elif p.stat == Status.OCCUPIED and p.key == key: # 해당 버킷이 쓰이는 중이며, 그 키값이 동일하다면 버킷을 리턴
                return p
            hash = self.rehash_value(hash) # 재해시시킨후 다른 버킷을 확인
            p = self.table[hash]
        
        return None
    
    def search(self, key: Any) -> Any:
        p = self.search_node(key) # 해당하는 버킷을 찾음
        if p is not None: # 버킷이 비어있지 않으면 값을 반환
            return p.value
        else: # 비어있으면 None 방환
            return None
    
    def add(self, key: Any, value: Any) -> bool:
        # 원소의 추가
        if self.search(key) is not None: # 넣으려는 원소의 키와 동일한 키의 원소가 이미 있으면 False
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]
        for _ in range(self.capacity): # 테이블을 돌면서
            if p.stat == Status.EMPTY or p.stat == Status.DELETED: # 비어있는 곳을 찾음
                self.table[hash] = Bucket(key, value, Status.OCCUPIED) # 버킷 값 넣음
                return True
            hash = self.rehash_value(hash) # 재해시 해서 반복
            p = self.table[hash]
        
        return False
    
    def remove(self, key: Any) -> bool:
        p = self.search_node(key) # 해당 해시값의 버킷찾음
        if p is None: # 버킷이 비어있다면
            return False
        p.set_status(Status.DELETED) # 비어있지 않으면 Status만 바꿈으로서 삭제
        return True
    
    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--미등록--')
            elif self.table[i].stat == Status.DELETED:
                print('--삭제 완료--')

