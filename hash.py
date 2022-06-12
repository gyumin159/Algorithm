# 해시법
# 해시법을 이용하면 검색, 추가, 삭제등을 적은 비용으로 할 수 있다.
# 흔히 추가나 삭제를 하기위해서는 O(n)만큼 소요되는데 해시법에서는 적게 소요된다.

# 해시법은 저장하려는 value의 해시값을 구해서 해당 해시값을 가진 테이블에 저장하는것인데
# 저장하려는 데이터가 많아질수록 필연적으로 value는 다르지만 같은 해시값을 가지는 일이 생겨
# 충돌이 발생하게 된다.

# 이에 대한 해결법으로 2가지가 있다
# 1. 체인법 -> 해시테이블에 연결리스트에 대한 주소를 저장하고 연결리스트에 값들을 저장하기
# 2. 오픈 주소법 -> 빈 버킷을 찾을 때까지 해시함수를 반복


from __future__ import annotations
import hashlib
from typing import Any


class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next

# 1. 체인법

class ChainedHash:
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key:Any) -> int:
        # 해시값 구함
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        # key가 동일한 원소를 검색하여 값을 반환
        hash = self.hash_value(key) # 받은 키를 해시값으로 바꿈
        p = self.table[hash] # 해당 해시값에 맞는 테이블로 이동
        
        while p is not None: # 해시 테이블의 포인터가 None이 아닌동안 연결리스트의 끝까지 가며 검색
            if p.key == key:
                return p.value
            p = p.next
        
        return None # 없는 경우 None 반환
    
    # 키로 원소를 검색하는 과정은 이렇다.
    # 키를 해시값으로 -> 해시값을 인덱스로하는 버킷에 주목 -> 버킷이 참조하는 연결리스트를 선형 검색하며 키값이 같은 노드를 찾음
    
    def add(self, key: Any, value: Any) -> bool:
        # 원소를 추가하기
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return False
            p = p.next
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    # 원소를 추가하는 과정은 이렇다
    # 키를 해시값으로 -> 해당 버킷에 주목 -> 해당 버킷의 연결리스트를 선형 검색하며 같은 키값을 가지는 노드가 있는지 확인 -> 없다면 새로운 노드(key, value, 기존노드에 대한 참조)를 생성후 버킷에 대입
    # 버킷의 맨 앞에 생성되게 되므로 temp = Node(key, value, self.table[hash]) 여기서 보이듯 기존 버킷이 참조하고 있던 노드인 self.table[hash]를 노드의 next값으로 넣어줘야 한다.
    
    def remove(self, key: Any) -> bool:
        # key가 동일한 원소 삭제
        hash = self.hash_value(key)
        p = self.table[hash] # 노드를 주목
        pp = None # 이전 노드를 주목
        
        while p is not None:
            if p.key == key:
                if pp is None: # 이전 노드가 없다. -> 버킷이 참조하는 노드 = 첫 노드
                    self.table[hash] = p.next # 현재 노드가 참조하는 다음노드를 버킷에 넣음으로서 p는 아무에게도 참조받지 않고 삭제됨.
                else: # 이전 노드가 있다.
                    pp.next = p.next # 이전 노드랑 p 다음노드랑 연결시킴. -> p는 삭제됨
                
                return True
            pp = p
            p = p.next
        
        return False
    
    # 원소를 삭제하는 과정은 이렇다.
    # 키를 해시값으로 -> 해당 버킷에 주목 -> 해당 버킷의 연결리스트를 선형검색 하면서 키와 같은 값이 발견되면 그 노드를 리스트에서 삭제.(아무도 그 노드를 참조하지 않게 만듬.)
    

    def dump(self) -> None:
        # 해시 테이블에 저장된 value들을 덤프
        for i in range(self.capacity):
            p = self.table[i] # 각각 버킷에 주목
            print(i, end='')
            while p is not None:
                print(f'  --> {p.key} ({p.value})', end='')
                p = p.next
            print()