
n, m = input().split()
matrix = [list(map(int, input().split())) for _ in range(int(n))]
res = [[row[i] for row in matrix] for i in range(int(m))]
for a, b in res:
    print(a, b)
