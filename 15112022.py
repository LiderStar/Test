def get_winner(ballots):
    from collections import Counter, defaultdict
    print(ballots)
    # lt = Counter(ballots).most_common(1)
    # t,y = list(*lt)
    d = defaultdict(int)
    for k in ballots:
        d[k] += 1

    if int(len(ballots)/2) < max(d.values()):
        return max(d, key=d.get)
    # if len(ballots) / 2 < y:
    #     return t
    # else:
    #     return None


print(get_winner(("A", "A", "A", "B", "B", "B", "A")))  # , "A")
print(get_winner(("A", "A", "A", "B", "B", "B")))  # , None)
print(get_winner(("A", "A", "A", "B", "C", "B")))  # , None)
print(get_winner(("A", "A", "B", "B", "C")))  # , None)

n = ['a','b','c','a','a','c','b']

l = enumerate(n)
print(l)
rew = [(v,k) for k,v in l ]
c = set(l)
print(rew)
c = set(rew)
print(c)
r,t = max(c)
print(max(c))
print(r)
print(t)
