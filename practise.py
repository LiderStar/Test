import re
def it(n):
    return str(n) == str(n)[::-1]



print(it(327 ))


for i in range(1,5):
    print(str(i)*i)


for i in range (1,11):
    for j in range(1,i):
        print(j, end=" ")
    print()

n = sum([i for i in range(16)])
print(n)

n = 44897497498798798798
print(len(str(n)))

for i in range (1,11):
    for j in range(11-i,0,-1):
        print(j, end=" ")
    print()



def inner(func):
    def wrapper(*args):
        func(*args)
        return func(*args) + 5
    return wrapper

@inner
def mul(a,b):
    return a+b

print(mul(5,6))   


def rec(n):
    if n:
        return n + rec(n-1)
    else:
        return 0
    
print(rec(10))



rem = [i for i in range(11 ,25) if i%2 == 0]
print(rem)

str = 'djfjjgf.knfghe;ndsmbdufhep[fe;lmdfjbgfuofjewjkfl,nfigfuierhipoergf'

data = {}

for i in str:
    data[i]= data.get(i,0)+1
print(data)


stre = 'Kelly Kelly Kelly Kelly Kellykjiojio poo j-0u900 Kellyi-0i-i0 Kelly-iu-0uiKelly Kelly ioji'
print(len(stre))
pattern = r'Kelly'
rez = re.finditer(pattern, stre)
n = []
for i in rez:
    n.append(i.span())
print(n[-1])


s = 'im 34 years 25 old'.split()
s_new  = list(filter(lambda x: x.isdigit(), s))
print(" ".join(s_new))