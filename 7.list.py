# %%

"""
리스트

배열
a = 1
b = 2
c = 3
fff = 100000
"""

a = [1, 2, 3, 4]
print(a)

b = ["1", True, False, 12, 1.5]
print(b)

a[0] = "다른 거"
print(a[0])

a.append(5)
print(a)

a.append(True)
print(a)

a.insert(2, "삽입")
print(a)

print(a.pop())
print(a)
print(a.pop(2))
print(a)

del a[0]
print(a)


# %%
"""배열 인덱싱"""

b = [0, 1, 2, 3, 4]

print(b[len(b) - 1])
print(b[-1])

c = "abcd"
print(c[-1])

# %%

"""
if 문에서 리스트
"""

a = []

if a:
    print("있음")
else:
    print("없음")

# %%
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""array slicing"""

print(a[2:6])
print(a[0:6])
print(a[:6])
print(a[7:])

print(a[::2])
print(a[1::2])
print(a[0:6:2])

print(a[0:-1])

print(a[::-1])  # 역순

# 팰린드팰
a = "abba"
print(a == a[::-1])

# %%
"""리스트의 얕은 복사"""
a = [0, 1, 2, 3, [1, 2, 3, 4]]
b = a[:]  # 복사
print(b)
import copy

b = copy.deepcopy(a)
b[-1][0] = "첫번째 원소"
print(b)
print(a)  # 얕은 복사, 깊은 복사

# %%
a = "abcd"

print(a[0])
print(a[1:3])
print(a[::2])
print(a[:])

# %%
"""
다차원 리스트
"""

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
[1,2,3]
[4,5,6]
[7,8,9]
"""

print(lst[2][2])

# %%
"""리스트 연산"""

"p" * 3
"ab" + "cd"
print([1, 2, 3] * 3)
print([1, 2, 3] + [4, 5])
