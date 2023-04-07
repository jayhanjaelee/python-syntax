import time

s = set()

for x in range(10000):
    s.add(x)

# print(s)

start_time = time.perf_counter()

# Your code goes here
print(5000 in s)

end_time = time.perf_counter()

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")
