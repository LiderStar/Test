import re

with open("dates.txt") as file:
    
    src = file.read()
    # print(src)
    res = re.finditer(r"\d\d.\d\d.\d\d\d\d", src)
    res = re.finditer(r"\d{2}.\d{2}.\d{4}", src)
    res = re.finditer(r"\d{2}/\d{2}/\d{4}", src)
    res = re.finditer(r"\d{2}-\d{2}-\d{4}", src)
    res = re.finditer(r"\d{2}\.\d{2}\.\d{4}", src)
    res = re.finditer(r"\d{2}[/-]\d{2}[/-]\d{4}", src)

    
    for i in res:
        print(i)
        print(i.span())



with open("emails.txt") as file1:
    rs = file1.read()

    pattern = r"(\S+)@(\S+)"
    res1 = re.finditer(pattern, rs)

    for i in res1:
        print(i.group())

with open("urls.txt") as file2:
    rs = file2.read()

    pattern = r"([a-z]+:))"
    pattern = r"https?://([a-zA-z]+)\."
    pattern = r"https?://([a-zA-z]+)\.([a-zA-Z0-9-]+)"
    pattern = r"https?://(www\.)?([a-zA-z]+)\.([a-zA-Z0-9-]+)"
   
    res2 = re.finditer(pattern, rs)

    for i in res2:
        print(i.group())
        # print(i.group(1))
        print("#" * 45)
        