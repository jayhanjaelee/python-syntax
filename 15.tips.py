# %%

"""
구조 분해 할당
"""

a = (1, 2, 3)
x, y, z = a

print(x, y, z)

# %%
"""
list comprehension
"""

a = [1, 4, 5, 6, 7, 10]

b = [x * 2 for x in a]
# for x in a:
#     b.append(x * 2)

pivot = 5
b = [x for x in a if x > pivot]

print("b: ", b)

# %%

"""
unpacking
"""

a = (1, 2, 3)
print(a)


def f(x, y, z, w):
    return x + y + z + w


x = ("1", "2", "3", "4")

y = [*(map(int, x))]
y = list((map(int, x)))
print("y: ", y)

print(f(1, *a))

z = {1: "손", 2: "흥", 3: "민", 1999: "최고"}
w = {**z}
z[1] = "갓"
print("z: ", z)
print("w: ", w)
print(id(z))
print(id(w))

# %%

"""
lambda
"""


def A(x):
    return x * x + x + 1


print(A(1))


def B(key, x):
    return key(x)


print(B(lambda x: x * x + x + 1, 1))

# %%
"""
global
"""

glo = 0


def function(a, b, c, d):
    print("glo: ", glo)


function(1, 2, 3, 4)
