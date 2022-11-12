import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)

def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)



def solution(s):
    new_line = ""
    for i in s:
        if i.islower():
            new_line += i
        elif i.isupper():
            new_line += " "+i
    return new_line

print(solution("helloWorld"))#, "hello World")
print(solution("helloworld"))#, "hello World")
print(solution("camelCase"))#, "camel Case")
print(solution("breakCamelCase"))#, "break Camel Case")
print(solution(""))#, "break Camel Case")
