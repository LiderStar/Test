import os
from pathlib import Path

path = Path("C://Windows")
path1 = Path("C://Windows/System32/cmd.exe")
path2 = Path("C://Windows")
p = path.exists()
p1 = path1.is_file()
p2 = path2.is_dir()
print(p)
print(p1)
print(p2)

# Path("directory").mkdir(parents=True, exist_ok=True)

if os.path.exists("directory"):
    print("ok")
else:
    os.makedirs('directory')


from zipfile import ZipFile
if not os.path.exists("zip_dir"):
    os.makedirs("zip_dir")

with ZipFile("zip_dir/all.zip", "w") as zf:
    for path in Path("directory").rglob("*.*"):
        zf.write(path)
