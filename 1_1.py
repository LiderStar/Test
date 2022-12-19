from itertools import groupby

n = '7717777'
tp = []
def chunk(n):
    tmp = []
    st = ""
    alfa = {2: 'a', 22: 'b', 222: 'c',
        3: 'd', 33: 'e', 333: 'f',
        4: 'g', 44: 'h', 444: 'i',
        5: 'j', 55: 'k', 555: 'l',
        6: 'm', 66: 'n', 666: 'o',
        7: 'p', 77: 'q', 777: 'r', 7777: 's',
        8: 't', 88: 'u', 888: 'v',
        9: 'w', 99: 'x', 999: 'y', 9999: 'z',
        0: " "}
    if "7" in n or "9" in n:
        for i in range(0, len(n), 4):
            tmp.append(n[i:i + 4])
        return tmp
    else:
        for i in range(0, len(n), 3):
            tmp.append(n[i:i + 3])
        return tmp
    #
    # for i in range(len(n)+1):
    #     if n[i] == n[i+1]:

x = ["".join(list(g)) for k, g in groupby(n) if k!='1']
for i in x:
    if len(i) > 4:
        tp.extend(chunk(i))
    else:
        tp.append(i)
print(x)
print(tp)

print(chunk('0000'))
# print(convert(""))
# print(convert(0000))
# print(convert(777777)) # = "sq".
# print(convert(7717777)) # = "qs".

ebomkxusmbv qelo j
ebomkxusmbv qelo j