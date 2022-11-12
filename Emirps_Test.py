def check(num):
    tmp = [i for i in range(1,(num//2)+1) if num % i == 0] 
    return True if len(tmp) == 1 else False


def find_emirp(n):
    n=int(n)    
    lst=[2,3,5,7,9]
    l = []
    if n <= 10:
        return [0,0,0]
    else:
        for i in range(11, n+1, 2):
            
            if (i%10==5):
                continue
            for j in lst:
                if i % j == 0:
                    break            
            else:
                lst.append(i)
    for i in lst[5:]:
        if i == int("".join(reversed(str(i)))):
            continue
        elif i in lst and check(int("".join(reversed(str(i))))):
            l.append(i)
            
    return [len(set(l)), max(set(l)),sum(set(l)) ]
    
print(find_emirp(500))