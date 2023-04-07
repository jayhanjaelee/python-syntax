# %%
# enumerate

a = [111, 222, 333, 444]

b = []

for i in range(len(a)):
    b.append((i, a[i]))

print(b)
print([*enumerate(a)])
y = list((map(int, a)))

# %%
# dictionary


d = {}
d["left"] = "left"
print(d)


d = {1: "a", 2: "b", 3: "c"}
print(d)
for x in d:
    print(x, d[x])

for x in d.items():
    print(x)

# 어떤 숫자가 dictionary 안에 key 로 존재하는지 확인
# in
print(1 in d)
print("a" in d.values())

# runtime error

if 3 in d:
    print("d: ", d[3])

# %%

# set

S = set([1, 1, 3, 3, 5, 5, 6, 7, 7, 7])  # 수학 집합 (중복 값 제거)
# set 은 index 로 접근 불가

# list 에 비해 탐색속도 빠름
print(S)

for x in S:
    print(x)


a = {1, 2, 3, 4, 5, 6}
print(3 in a)
