n = 1
def is_happy(n):
    tmp = []
    while n != 1:
        n = sum([int(i)**2 for i in list(str(n))])
        if n in tmp:
            return False
        else:
            tmp.append(n)
    return [1,2,3,4,5]

print(is_happy(n))
        

