x = [1, 2, [3, 4, 5]]
y = x.copy()

x[0] = 5
print(x, y) # [5, 2, [3, 4, 5]] [1, 2, [3, 4, 5]]

x[2][0] = 7
print(x, y) # [5, 2, [7, 4, 5]] [1, 2, [7, 4, 5]]

# 파이썬의 .copy() 메소드는 얕은 복사로, y는 x[0], x[1], x[2] 가 참조하는 곳까지 복사한다 -> y[0] 은 1 참조, y[1]은 2참조, y[2]는 [3, 4, 5] 참조
# 따라서 x[0]이 바뀌었을 때는 값이 변하지 않았지만
# x[2]가 참조하는 곳인 [3, 4, 5]의 값이 변했을 때는 값이 변화했다. y또한 같은 리스트를 참조하기 때문

import copy

x1 = [1, 2, [3, 4, 5]]
y1 = copy.deepcopy(x1)

x1[2][0] = 7
print(x1, y1) # [1, 2, [7, 4, 5]] [1, 2, [3, 4, 5]]

# deepcopy의 경우 피상적인 참조값 뿐만 아니라 참조하는 객체 자체를 복사. y1[2] 는 [3, 4, 5] 에 참조하는게 아닌 y[2][0] = 3, y[2][1] = 4 , .. 이런식으로 깊숙히 참조한다
# 즉 객체가 갖는 모든 멤버를 복사한다.
