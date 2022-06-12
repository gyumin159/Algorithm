# def med3(a, b, c):
#     if a >= b:
#         if b >= c:
#             return b
#         elif a >= c:
#             return c
#         else:
#             return a
#     else:
#         if b <= c:
#             return b
#         elif a <= c:
#             return c
#         else:
#             return a


# print(med3(1, 2, 3))
# print(med3(1, 3, 2))
# print(med3(3, 2, 2))
# print(med3(3, 3, 2))
# print(med3(1, 3, 1))


# def med3_1(a, b, c):
#     if (b >= a and c <= a) or (b <= a and c >= a):
#         return a
#     elif (a > b and c < b) or (a < b and c > b):
#         return b
#     return c


# 1부터 n까지 정수의 합 구하기.


# def sum_n(n):
#     sum = 0
#     i = 1

#     while i <= n:
#         sum += i
#         i += 1
#     return sum

# def sum_n1(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum


# 연속하는 정수의 합을 구하기

# def sum_ab(a, b):
#     if a > b: # range를 이용할 것이기 때문에 오름차순으로 정리를 해야한다.
#         a, b = b, a
#     sum = 0
#     for i in range(a, b + 1):
#         if i < b: # for 문을 도는 만큼, if문을 통해 조건을 확인해야함. 상당히 비효율적.
#             print(f"{i} + ", end='')
#         else:
#             print(f"{i} = ", end='')
#         sum += i

#     print(sum)


# def sum_ab1(a, b):
#     if a > b:
#         a, b = b, a
#     sum = 0
#     for i in range(a, b):
#         print(f"{i} + ", end='')
#         sum += i
#     sum += b
#     print(f"{b} = {sum}")


# sum_ab1(3, 7)


# +와 - 를 번갈아 n번 출력하기.

# def plus_minus(n):
#     print('-+' * (n//2), end='')
#     print('-' * (n%2))

# plus_minus(6)

# *을 n개 출력하며 w개마다 줄바꿈하기

# def test(n, w):
#     for i in range(n):
#         print('*', end='')

#         if i % w == w - 1:
#             print()

#     if n % w:
#         print()

# test(7, 5)

# def test1(n, w):
#     print(('*'*w + '\n') * (n//w), end='')
#     print('*' * (n%w), end='')

# test1(3, 5)


# while True:
#     n = int(input("양의 정수만 입력하세요. :"))
#     if n > 0:
#         break

# import random

# n = int(input('생성하고 싶은 난수의 수 :'))
# for i in range(n):
#     r = random.randint(10, 99)
#     print(r, end=' ')
#     if r == 13:
#         print('13 발생 종료')
#         break
# else:
#     print('생성완료')  # for else 나 while else 는 반복문이 완전하게 실행된 후에 else구문을 실행한다. 만약에 break걸리면 실행 하지 않는다.


# 다중 루프

# print('-' * 27)
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i*j:3}', end='')
#     print()


# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for i in range(n):
#     for _ in range(n - (i + 1)):
#         print(' ', end='')
#     for _ in range(i+1):
#         print('*', end='')
#     print()

# l = [None] * 5


# n = int(input())

# for i in range(1, n + 1):
# 	print((' ' * (n - i)) + '*' * i)


# import itertools 조합에 관련된 툴이 있다.

# setting = input().split(' ')
# int_setting = list(map(int, setting))

# nums = [None] * int_setting[0]
# nums = input().split(' ')
# int_nums = list(map(int, nums))


# it = itertools.combinations(int_nums, 3)
# sums = []
# for i in it:
#     sums.append(sum(i))

# for e in sums:
#     if e <= int_setting[1]:
#         prev = e
#         break
# for i in range(len(sums)):
#     if prev <= sums[i] <= int_setting[1]:
#         prev = sums[i]

# print(prev)


# 소수 출력하기 v1

# counter = 0

# for n in range(2, 1001):
#     for i in range(2, n):
#         counter += 1
#         if n % i == 0:
#             break

#     else:
#         print(n)
# print(counter)

# 어떤 수가 2 로 나누어 떨어지지 않는다면, 4나, 6 이나, 8등 2를 포함한 합성수들로도 나누어 떨어지지 않을거다
# 또 마찮가지로 3으로 나누어 떨어지지 않는다면, 6 , 9 , 12 등 3을 포함한 합성수들로도 나누어 떨어지지 않을거다.
# 결국에는 소수란 2부터 n-1까지의 다른 소수들에게 나누어 떨어지지 않는다면, 그것은 소수다.
# 소수가 아닌 수들은 소수로 이루어진 합성수이니까

# 소수 출력하기 v2

# counter = 0
# ptr = 0 # 배열안에 소수의 갯수

# prime = [None] * 500
# prime[ptr] = 2
# ptr += 1

# for n in range(3, 1001, 2):
#     for e in range(1, ptr): # 홀수들만을 대상으로 하기 때문에 2로는 나눌 필요가 없어서 range(1, ptr)
#         counter += 1
#         if n % prime[e] == 0:
#             break
#     else:
#         prime[ptr] = n
#         ptr += 1


# for i in prime:
#     print(i)
# print(counter)


# n을 직사각형의 넓이라고 생각해보면, i*j = n 이런식으로 두변의 곱 = 넓이 라고 할 수 있을거다.
# n = 100 일때를 생각해보자. 100 = 2*50, 4*25, 5*20, 10*10, 20*5, 25*4, 50*2 이렇게 표현될 수 있는데
# 10*10을 기준으로 대칭적이란것을 알 수 있다.
# n = a*b 일때 n이 a로 나누어 떨어지지 않는다면, b로도 나누어 떨어지지 않을거다.
# 따라서 a나b 한 변으로만 나눗셈을 시도해 봐도 되며 한 변이 n의 제곱근보다 크다면 대칭을 넘어 위치만 바뀐 같은 걸 반복하고 있는 것일거다

# 결론은 n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는다면 그것은 소수다\


# 소수 출력하기 v3

# counter = 0
# ptr = 0
# prime = [None] * 500

# prime[ptr] = 2
# ptr += 1
# prime[ptr] = 3
# ptr += 1

# for n in range(5, 1001, 2):
#     i = 1
#     while prime[i] * prime[i] <= n:
#         counter += 2
#         if n % prime[i] == 0:
#             break
#         i += 1
#     else:
#         prime[ptr] = n
#         ptr += 1
#         counter += 1

# for i in range(ptr):
#     print(prime[i])
# print(counter)


