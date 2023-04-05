# %%
import math

"""format"""

"{}, {}".format(1, "중요한")
"{1}, {0}".format(1, 2)

"{:.2f}".format(math.pi)
"{:.3f}".format(math.pi)
# %%

"""split"""

print("1 2 3 4 5 6 7 8".split())
a = "1.5,2,3,4,5,6,7,8".split(",")
b = list()

b = list(map(float, a))

# %%
