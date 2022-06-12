from enum import Enum
from hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료']) # 메뉴

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13) # 버킷의 수가 13개인 해시테이블 생성

while True:
    menu = select_menu()
    
    if menu == Menu.추가:
        key = int(input('추가할 키 입력 :'))
        val = input('추가할 값 입력 :')
        if not hash.add(key, val):
            print('추가에 실패')
    
    elif menu == Menu.삭제:
        key = int(input('삭제할 키 입력 :'))
        if not hash.remove(key):
            print('삭제에 실패')
    
    elif menu == Menu.검색:
        key = int(input('검색할 키 입력 :'))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키에 해당하는 값은 {t} 입니다')
        else:
            print('검색한 키에 해당하는 값이 없습니다.')
    
    elif menu == Menu.덤프:
        hash.dump()
    
    else:
        break