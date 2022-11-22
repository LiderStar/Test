
from itertools import groupby

def chunk(n):
    tmp = []
    if "7" in n or "9" in n:
        for i in range(0, len(n), 4):
            tmp.append(n[i:i + 4])
        return tmp
    else:
        for i in range(0, len(n), 3):
            tmp.append(n[i:i + 3])
        return tmp

def convert(n):
    tp = []
    st = ""
    alfa = {2: 'a', 22: 'b', 222: 'c',
            3: 'd', 33: 'e', 333: 'f',
            4: 'g', 44: 'h', 444: 'i',
            5: 'j', 55: 'k', 555: 'l',
            6: 'm', 66: 'n', 666: 'o',
            7: 'p', 77: 'q', 777: 'r', 7777: 's',
            8: 't', 88: 'u', 888: 'v',
            9: 'w', 99: 'x', 999: 'y', 9999: 'z'
            }

    x = ["".join(list(g)) for k, g in groupby(n) if k!='1']
    for i in x:
        if len(i) >= 4:
            tp.extend(chunk(i))
        else:
            tp.append(i)

    for i in tp:
        if sum([int(j) for j in i]) == 0:
             st += " " * len(i)
        elif int(i) in alfa:
             st += alfa[int(i)]
    print(tp)
    return st


print(convert('3322666655998877776228880773355566605'))


import re
def phone_words(str):
    ansd = {'0':' ','2':'a','22':'b','222':'c','3':'d','33':'e','333':'f',\
           '4':'g','44':'h','444':'i','5':'j','55':'k','555':'l','6':'m',\
           '66':'n','666':'o','7':'p','77':'q','777':'r','7777':'s','8':'t','88':'u',\
           '888':'v','9':'w','99':'x','999':'y','9999':'z'}
    ans=''
    for i in re.findall('0|2{1,3}|3{1,3}|4{1,3}|5{1,3}|6{1,3}|7{1,4}|8{1,3}|9{1,4}',str):
        ans+=ansd[i]
    return ans