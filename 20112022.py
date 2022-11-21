from itertools import groupby


def convert(n):

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

    x = [j[0] * len(j) for j in [list(g) for k, g in groupby(str(n))] if j[0] != '1']
    for i in x:
        if int(i) in alfa:
            st += alfa[int(i)]
        if len(i) > 4:
            if int(i[:4]) in alfa:
                st += alfa[int(i[:4])] + alfa[int(i[4:])]
            else:
                st += alfa[int(i[:3])] + alfa[int(i[3:])]
    print(x)
    return st


print(convert(443355555566604466690277733099966688))
print(convert(""))
print(convert(000))
print(convert(777777)) # = "sq".
print(convert(7717777)) # = "qs".
