# %%
import itertools

a = [1, 3, 5]

print(*itertools.combinations(a, 2))  # 조합 경우희 수 출력
print(*itertools.combinations_with_replacement(a, 2))  # 중복 조합 경우희 수 출력
print(*itertools.permutations(a, 2))  # 순열 경우희 수 출력
print(*itertools.product(a, a))  # 두 배열의 가능한 모든 경우의 수 출력
print(*itertools.product(a, repeat=3))
