from itertools import chain, combinations
A = {1, 2, 3, "A", "B", "C"}
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
print(list(powerset(A)))