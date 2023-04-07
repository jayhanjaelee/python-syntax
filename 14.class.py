# %%

"""

클래스

객체지향, 인스턴스
abcd

다형성, 캡슐화
"""


class A:
    def __init__(self, name, number, score) -> None:
        self.name = name
        self.number = number
        self.score = score

    def to_string(self):  # method
        return "name: {}, number: {}, score: {}".format(
            self.name, self.number, self.score
        )

    def example(a, b):  # static method
        return a.number < b.number


a = A("한재", "3", "100")

print(vars(a))
print(a.name, a.number, a.score)

b = A("hanjae", "4", "0")
print(b.name, b.number, b.score)
print(b.to_string())

A.example(a, b)
