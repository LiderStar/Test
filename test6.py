# n = 'my file name.txt'.split()
# print("_".join(n))

# print(re.sub('\s+', '_', input().strip()))

n = list(map(int, input().split()))
res = {}
for i in n:
    res[i] = res.get(i,0)+1
print(*(k for k,v in res.items() if v > 1))