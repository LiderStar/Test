import re

pattern = '.a.'

string = "tan"

print(re.match(pattern, string))

###########################################################################
result = re.finditer('[dk]', "fsdkljflkdsjfdshfjdhsofdhysfpohsdkf") 
result = re.finditer('[^dk]', "fsdkljflkdsjfdshfjdhsofdhysfpohsdkf") # исключает
result = re.finditer('.', "123") 
result = re.finditer('..', "123") 
for i in  result:
    print(i)

###########################################################################
result1 = re.finditer("^a", "alfa")  # start with ^
for i in result1:
    print(i)


result2 = re.finditer("a$", "alfa")  # end with a $
for i in result2:
    print(i)

#("ma*n") # -> like maaaaan, mn, man, -> not like main, men

###########################################################################
result3 = re.finditer("ma+n", "man")
# + one ore more a
# ? zero or one "ma?n" 
# "a{2,4}" aa, aaa, aaaa -> match     a, aaaaa -> not match
# [1-9]{2,4} 11, 1234, 3456, 25 .... -> match 1, 2, - > not match  25678 -> 2567


for i in result3:
    print(i)
###########################################################################
result4 = re.finditer("a|b", "adc") # a or b
# (a|b|c)xz - > axz bxz cxz  abcxz -> not matc

for i in result4:
     print(i)


###########################################################################
string = "Hello 65 dlfjgkl; 89 kfjglk89ljlhjkgfds6dsfnb5"
pattern = "\d+" # [0-9]
res = re.findall(pattern, string)
print(res)

###########################################################################
pattern = "\d+"

print(re.split(pattern, string))

###########################################################################
string = "abc 12 de 23 \n f45 621"
print(string)
pattern = "\s+" # all whitespaces one ore more

print(re.findall(pattern,string))

replace = ""

print(re.sub(pattern,replace,string)) # убрали все пробелы и переносы строк

###########################################################################
# match - ищет в начале, search - ищет везде \A - искать в начале
string = "python and fun"
pattern = "\Apython"

print(re.search(pattern, string))

###########################################################################
string = "125 48489 46549847, 161894894 12165498, 13465465 4464643"

pattern = "(\d{3}) (\d{4})"

match = re.search(pattern, string)

if match:
    print(match.group())

# match.start()
# match.end()
#match.span()
#\d - [0-9]
#\D - [a-zA-Z_]
#\s - space tab \n
#\S - [a-zA-Z_0-9]

###########################################################################
###########################################################################

