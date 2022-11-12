
# n, m = input().split()
# matrix = [["." if (i + j) % 2 == 0 else "*" for j in range(int(m)) ] for i in range(int(n))]
# print(*(' '.join(i) for i in matrix), sep="\n")


# n = int(input())
# matrix = [["0" for i in range(n)] for j in range(n)]
# print(*(' '.join(i) for i in matrix), sep="\n")
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             matrix[i][j] = "1"
#         elif i+j >= n:
#             matrix[i][j] = "2" 
# print(*(' '.join(i) for i in matrix), sep="\n")


# n = int(input())
# lt = iter(list(range(1,n*n+1)))
# print(lt)
# matrix = [[ str(next(lt)) for i in range(n)] for j in range(n)]
# print(*(' '.join(i) for i in matrix), sep="\n")


# n, m = input().split()
# lt = iter(list(range(1,int(n)*int(m)+1)))
# matrix = [[ str(next(lt)) for i in range(int(n))] for j in range(int(m))]
# result = [[matrix[j][i].ljust(3) for j in range(len(matrix))] for i in range(len(matrix[0]))]

# print(*(' '.join(i) for i in result), sep="\n")

# n = int(input())
# matrix = [["0" for i in range(n)] for j in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             matrix[i][j] = "1"
#         elif i == j:
#             matrix[i][j] = "1" 
# print(*(' '.join(i) for i in matrix), sep="\n")


# n = int(input())
# res = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]
# for x in res:
#     print(*x)

# ШАХМАТНАЯ ДОСКА######################################

# xy = input()
# matrix = [["." for i in range(8)] for j in range(8)]
# y = '87654321'.index(xy[1])
# x = 'abcdefgh'.index(xy[0])
# matrix[y][x] ='N'
# for i in range(8):
#     for j in range(8):
#         INX = (y - j) * (x - i)
#         if INX == 2 or INX == -2:
#             matrix[j][i] = '*'
# for x in matrix:
#     print(*x)


n = int(input())
matrix = [input().split() for j in range(n)]
matrix_list = sum(matrix, [])
if len(set(matrix_list)) == n ** 2 and '0' not in matrix_list:
    row = [sum(list(map(int,x))) for x in matrix]
    colum = [sum(list(map(int,x))) for x in zip(*matrix)]
    # diag = [((list(map(int, matrix[i][j])) for i in range(n) if i == j) for j in range(n))]
    diag = [[matrix[i][j] for i in range(n) if i == j] for j in range(n)]
    diag_sm = [sum(map(lambda x: int(*x), diag))]
    diag_2 = [[matrix[i][j] for i in range(n) if i+j == n-1] for j in range(n)]
    diag_2_sm = [sum(map(lambda x: int(*x), diag_2))]
    print(row)
    print(colum)
    print(diag_sm)

    print(diag_2_sm)

    print("YES" if row == colum == diag_sm*n == diag_2_sm*n else "NO")
else:
    print("NO")

