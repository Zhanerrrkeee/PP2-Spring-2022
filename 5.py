import itertools
def solve(s):
    perm = itertools.permutations(s, len(s))
    for i in perm:
        print((i))

solve(input())