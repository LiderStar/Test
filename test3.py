from asyncore import write
import os

with open("1.txt") as f1:
    with open("2.txt") as f2:
        for i,j in zip(f1,f2):
            a = i.strip(), "\t", j.strip()
            if not os.path.isdir('data'):
                os.makedirs('data')
                
            else:
                with open("data/test4.txt", "a") as file:
                    file.write(str(a))
