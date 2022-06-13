from typing import Any


class FixedQueue:
    # 크기가 고정된 큐를 링버퍼로 구현
    # 예외처리 두가지 Full, Empty

    class Full(Exception):
        pass

    class Empty(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.que = [None] * capacity
        self.capacity = capacity
        self.no = 0  # 현재 데이터 개수
        self.front = 0  # 맨 앞 원소의 커서
        self.rear = 0  # 맨 뒤 원소의 커서

    def __len__(self) -> int:  # 큐에 있는 데이터 개수 반환
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, value: Any) -> None:
        # 데이터를 인큐
        if self.is_full():  # 꽉 차있으면 에러
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity: # 만약에 인큐하기전 rear가 배열의 맨 끝에 있다면, + 1 했을때 인덱스 범위를 넘어가게 된다. 따라서 배열의 맨 끝과 맨 앞이 연결된 링모양을 만들려면 다시 0(맨앞)으로 보내줘야 한다
            self.rear = 0
        
    def deque(self) -> Any:
        # 데이터를 디큐
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1 # 다음 원소의 인덱스
        self.no -= 1
        if self.front == self.capacity: # enque와 마찬가지로 링모양을 구현하기 위해 0으로 세팅
            self.front = 0
        return x
    
    def peek(self) -> Any:
        # 맨 앞에 있는 데이터를 반환
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value : Any) -> int:
        # value와 같은 데이터가 포함되어 있는 위치를 반환
        # front 에서 rear로 선형검색
        # 하지만 링모양이기 때문에 인덱스값이 연속적이지 않을거고 따라서 (i + front) % capacity를 인덱스로 한다.
        for i in range(self.no): # 데이터의 개수만큼 반복
            idx = (self.front + i) % self.capacity
            if self.que[idx] == value: # front는 고정되어있고 첫번째 원소의 인덱스를 가르키고 있을거다. 거기에 i를 더해 다음 원소로 이동하는데 그 크기가 capacity보다 크거나 같아질 수 있으니 capacity로 나눠준다.
                return idx
        return -1
    
    def count(self, value : Any) -> int:
        # 큐안에 value의 개수를 구해서 반환
        c = 0
        for i in range(self.no): # 모든 데이터를 선형검색
            idx = (self.front + i) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c
    
    def __contains__(self, value: Any) -> bool:
        return self.count(value)
    
    def clear(self) -> None:
        # 모든 데이터가 no, front, rear를 이용해서 들어오고 나가기 때문에 이들을 초기화 해주면 삭제한것과 같다.
        self.no = 0
        self.front = 0
        self.rear = 0
    
    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            for i in range(self.no): # 모든 데이터를 맨 앞부터 출력
                print(self.que[(self.front + i) % self.capacity], end=' -> ')
            print()