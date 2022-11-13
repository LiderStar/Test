from gmpy2 import is_prime
def find_emirp(n):
    a = [i for i in range(13,n+1,2) if is_prime(i) and is_prime(int(str(i)[::-1])) and str(i)!=str(i)[::-1]]
    return [0,0,0] if not a else [len(a), max(a), sum(a)]

###############################################################

def chk_prime(x):
    if x % 2 == 0: return False
    for i in range(3, int(x**0.5+1), 2):
        if x % i == 0:
            return False
    return True

def gen_primes(n):
    return [x for x in range(3, n, 2) if chk_prime(x)]

all_primes = set(gen_primes(1000000))

def find_emirp(n):
    primes = [x for x in all_primes if x < n]
    emirps = [x for x in primes if int(str(x)[::-1]) in all_primes and x != int(str(x)[::-1])]
    return [len(emirps), max(emirps), sum(emirps)]

##############################################################

def prime_seive(n):
    start = range(n)
    for i1 in start:
        if i1 > 1:
            for i2 in range(i1*2,n,i1):
                start[i2] = 0
    return [i for i in start if i > 1]

def prime(n):
    if n % 2 == 0 or n < 3:return n == 2
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:return False
    return True


def find_emirp(n):
    primes = prime_seive(n)
    emirps = [i for i in primes if prime(int(str(i)[::-1])) and i != int(str(i)[::-1])]
    return [len(emirps),emirps[-1] if len(emirps) > 0 else 0,sum(emirps)]