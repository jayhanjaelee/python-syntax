# %%
import bisect
import random

# 이분 탐색
# 정렬된 배열에서 X를 찾아야 한다. 원래는 N 개만큼 탐색해야하는데 logN 으로 줄일 수 있다.

a = [random.randint(0, 100) for _ in range(10)]
print(a)
print(a[bisect.bisect_left(a, 10)] == 10)
