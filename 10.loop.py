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

# %%

"""
while loop
무한 반복 주의
"""

# i = 0
# cnt = 100
# while i < 10:
#     print(i)
#     cnt -= 1
#     if cnt == 0:
#         break

# while True:
#     menu = input("좋아하는 메뉴를 입력하세요.")
#     if menu == "김치":
#         print("good")
#     elif menu == "나가자":
#         print("나갔다.")
#         break
#     else:
#         print("bad")

lst = list(range(100))

while lst:
    a = lst.pop()
    print(a)

# %%

"""
for loop else

for 반복문이 정상적으로 종료되면
else 블록이 실행된다.
"""

i = 0
while i < 10:
    print(i)
    if i == 9:
        break
    i += 1
else:
    print("here")

# %%
