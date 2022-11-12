SPACE = ' '
STRAR = '*'

rows = 5
spaces = rows-1
stars = 1
for i in range(rows):
    if i < int(rows/2):
        print((SPACE*spaces) + (STRAR*stars) + (SPACE*spaces))
        stars += 2
        spaces -= 1
    else:
        print((SPACE * spaces) + (STRAR * stars) + (SPACE * spaces))
        stars -= 2
        spaces += 1

def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None