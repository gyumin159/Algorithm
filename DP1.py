# 동적 프로그래밍
# 피보나치 수열을 재귀함수로서 구현했다고 생각하자.

def fr(n : int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    fn = fr(n - 1) + fr(n -2)
    return fn
# F(4) = F(3) + F(2) => F(2) + F(1) + F(1) + F(0) => F(1) + F(0) + F(1) + F(1) + F(0)
# 위와같은 과정을 거치면서 문제를 해결하게 될텐데
# 문제점은 F(4)를 해결하기 위해 F(2)가 2번, F(1) 이 3번 .. 이런식으로 문제의 크기가 작아진 하위 객체가 중첩되서 생긴다.
# Top-Down Approach 인 재귀함수는 위와같은 문제점이 있고 이를 해결하기 위한 방법이 동적 프로그래밍이다.

# 동적 프로그래밍의 Memoization은 Bottom-Up Approach 로써 아래에서부터, 즉 작은 문제부터 해결해간다.
# Memoization 은 아래에서 부터 해결한 문제의 값을 저장해두어서 큰문제를 해결할 때 사용하는 방법이다.
# Memoization을 재귀함수에 접목시켜 문제를 해결할 수도 있다.

def f(n : int) -> int:
    dicf = {}
    dicf[0] = 0
    dicf[1] = 1
    
    for i in range(2, n + 1): # 2부터 n까지 다가간다
        dicf[i] = dicf[i - 1] + dicf[i - 2]
    return dicf[n]
