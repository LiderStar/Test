import string
with open("Test/text.txt", "r", encoding="utf-8") as file:
    src = file.readlines()
    for i in src:
        if i.startswith("d"):
                print(string.capwords(i).strip(), sep="")


s = "All that glitters is not gold"
print(s[9:-9])
print(s[::10])
print(s[:-4:-1])