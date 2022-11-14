import re
string = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.'''
pattern = '.*?l...'
res = re.findall(pattern, string) 
print(res)