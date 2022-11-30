import itertools


def sm(n):
    return sum(int(i) for i in str(n))


def num(n):
    for i, k in enumerate(list(range(9,1,-1)),2):
        if i == n:
            return k**n
print(num(3))
