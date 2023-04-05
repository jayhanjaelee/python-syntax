# %%

"""for loop"""

"""
학생 1
학생 2
학생 3
"""

"""
학생 100
"""

a = [1, 2, 3, 4]

합 = 0
for x in a:
    합 += x
    print("x: ", x)

print(합)

"""최솟값을 구하기"""

최솟값 = 1010101101010
for x in a:
    if x < 최솟값:
        최솟값 = x
print(최솟값)

최대값 = 0
for x in a:
    if x > 최대값:
        최대값 = x
print("최대값: ", 최대값)

# %%

"""
range
"""

# for x in range(10):
#     print(x)

# for _ in range(100):
#     print("백번 해봐")

for x in range(10, -1, -2):
    print(x)

# %%
"""
리스트 내부에 어떠한 원소가 있는지?
"""

arr = [0, 4, 6, 8, 10, [0, 3, 6]]

check = False
for x in arr:
    if x == 4:
        check = True

print(check)
print(4 in arr)

print("h" in "hello")

print("this: ", [0, 3, 5] in arr)

# %%
"""리스트, range, 순차적 접근"""

"""튜플"""

a = (0, 1, 2, 3)
for x in a:
    print(x)
