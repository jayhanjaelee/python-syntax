# %%

"""
문법 에러 (Syntax Error) -> Compile error
실행 전에 알 수 있는 에러

런타임 에러 (Runtime Error) -> Run time erro
실행 중에 발생하는 에러
"""

# if True:  문법에러

# a = None

# print(a.split())  # 런타임 에러 -> 실행 전에 알 수 없는 에러

b = [1, 2, 3, 4]
print(b[4])  # 런타임 에러

# %%

"""
try except
"""

x = None
try:
    raise IndexError()
    print("실행 구문")
except:
    print("예외 발생!")
else:
    print("정상 실행")
finally:
    print("무조건 실행")

# %%
"""
raise 응용
다중 for loop 탈출하기 raise 로 가능
"""


try:
    for i in range(10):
        for j in range(10):
            if j == 5:
                raise
            print(i, j)
except:
    pass

# %%
"""
함수 내에서 finally
return 해도 finally 는 반드시 호출
"""


def f():
    try:
        return
    except:
        pass
    else:
        print("else")
    finally:
        print("finally")


f()
