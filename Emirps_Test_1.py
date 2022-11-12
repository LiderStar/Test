def check(num):
    
    for i in range(1,num+1):
        if num%i != 0:
            return False
        else:
            return True
        
    # tmp = [i for i in range(1,num+1) if num % i == 0] 
    # return True if len(tmp) == 2 else False

n=int(input())    
lst=[2,3,5,7,9]
l = []
if n <= 10:
    print [0,0,0]
else:
    for i in range(11, n+1, 2):
        q = (n**0.5)+2
        if (i%10==5):
            continue
        for j in lst:
            if q > i:
                break
            if i % j == 0:
                break            
        else:
            lst.append(i)
for i in lst[5:]:
    if i == int("".join(reversed(str(i)))):
        continue
    elif i in lst and check(int("".join(reversed(str(i))))):
        l.append(i)
        # l.append(int("".join(reversed(str(i)))))
print(lst[5:])
print(len(lst[5:]))

print(set(l))
print(max(set(l)))
print(len(set(l)))
print(sum(set(l)))


print(check(37))