# 4.58s
# a = 0
# for _ in range(100000000):
#     a += 1


# 2.11s
def main():
    a = 0
    for _ in range(100000000):
        a += 1

    print(__name__)


if __name__ == "__main__":
    main()
