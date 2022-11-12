def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

def find_emirp(n):
    n=int(n)
    tmp = [2]   
    result = []
    if n <= 10:
        return [0,0,0]
    else:
        for num in range(3, n+1, 2):
            if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
                tmp.append(num)
                if num == int("".join(reversed(str(num)))):
                    continue
                elif num and is_prime(int("".join(reversed(str(num))))):
                    result.append(num)
            
    return [len(set(result)), max(set(result)),sum(set(result)) ]
    
print(find_emirp(1000000))