# %%
# stack 뒤에 넣고, 뒤에서 뺴는 자료구조

a = []  # list 는 스택
a.append(0)
a.pop()


# %%
# queue 뒤에 넣고, 앞에서 빼는 구조

b = []
b.append(0)
b.pop(0)

# pop(0) 단점: O(n) 시간복잡점
# '1 2 3 4 5' -> 원소 갯수만큼 탐색하고 맨 앞의 원소를 제거한다.

from collections import deque  # 덱으로 queue 구현

c = deque()
c.append(1)
print(c)
c.appendleft(2)
print(c)
c.pop()
print(c)
c.popleft()
print(c)

# 앞에서 원소 추가 ->  appendleft
# 앞에서 원소 제거 -> popleft
