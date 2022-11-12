import re

data = "cat"
pattern = ".a."
result = re.match(pattern, data)
print(result)

################################EXAMPLE#########################
match_result = re.finditer("[abc]", "adgtcffhghfgb")

for i in match_result:
    print(i)
    



################################EXAMPLE#########################
################################EXAMPLE#########################
################################EXAMPLE#########################
################################EXAMPLE#########################