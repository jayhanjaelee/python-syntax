# %%
a = [1, 2, 3, 4, 5]

b = [*map(lambda x: x * x, a)]  # map
print("b: ", b)

c = [x * x for x in a]  # list comprehension
print("c: ", c)

# map 은 훨씬 더 복잡한 기능을 제공한다. 함수 사용가능 하기 때문.
