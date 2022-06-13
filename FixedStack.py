import re
from typing import Any


class FixedStack:
    # 크기가 고정된 스택클래스
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity # 전달받은 인자로 배열의 크기 설정
        self.capacity = capacity
        self.ptr = 0 # 현재 스택안에 있는 데이터의 수를 나타내는 포인터
        
    def __len__(self) -> int:
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
    
    def push(self, value: Any) -> None:
        # 스택에 데이터를 넣음
        if self.ptr >= self.capacity:
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> Any:
        # 스택에서 데이터를 꺼냄
        if self.ptr <= 0:
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        # 꼭대기에 있는 데이터를 peek
        if self.ptr <= 0:
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]
    
    def clear(self) -> None:
        # 스택을 비움
        self.ptr = 0 # 스택에 데이터를 넣고 빼고 하는 일은 모두 ptr값에 의해 이루어지기 때문에 실제로 배열 원솟값을 변경할 필요가 없다.
    
    def find(self, value: Any) -> Any:
        # value가 들어있는지 확인하고 인덱스값을 반환, 없으면 -1 반환
        # 꼭대기 부터 바닥으로 선형검색하면서 찾음
        for i in range(self.ptr - 1, -1, -1): # range(a, b, c) -> a부터 b-1까지 c스텝씩 인데 역순으로 갈때는 range(10, 0, -1) 이렇게 하면 10부터 1까지 출력된다. 즉 0은 출력안됨
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value: Any) -> int:
        # 스택에 있는 value의 개수를 반환
        c = 0
        for i in range(self.ptr): # 바닥부터 선형검색
            if self.stk[i] == value:
                c += 1
        return c
    
    def __contains__(self, value: Any) -> bool:
        # value가 스택에 들어있는지 확인
        return self.count(value) > 0
    
    def dump(self) -> None:
        # 바닥부터 꼭대기로 데이터들을 출력
        if self.is_empty():
            print('No Data in Stack')
        else:
            print(self.stk[:self.ptr])