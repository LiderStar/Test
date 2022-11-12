
n = input().split()
result = [[]]
top = []

for i in range(len(n)+1):
    for j in range(len(n)+1):
        top = n[j:i+j+1]
        if len(top) == i+1:
            result.append(top)
    

print(result)    