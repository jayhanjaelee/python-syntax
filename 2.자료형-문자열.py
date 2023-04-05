# %%

"""
기본 자료형
"""
print(type(1))  # 정수 숫자
print(type(1.5))  # 실수
print(type(True))  # Boolean -> 참, 거짓
print(type(False))
print(type("문자열"))


# %%
"""문자열 만들기"""

print("중요한 것은 꺽이지 않는 마음")
print("'중요한 것은 꺽이지 않는 마음'")
print('"중요한 것은 꺽이지 않는 마음"')

# 이스케이프 문자 (탈출 문자)
print('"\'중요한 것은 \n꺽이지 않는 마음"')
print(
    """\
중요한 것은
꺽이지 않는 마음\
"""
)


# %%
"""문자열 연산"""
print("중요한 것은" + "꺾이지 않는 마음")
print("중요한 것은," * 3 + "꺽이지 않는 마음")

print("내가 간 곳은" + str(3) + "번지였다.")

print(int("3"))
print(len("abcd"))
