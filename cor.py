# import csv

# with open("data/data.csv") as file:
#     src_r = csv.reader(file, delimiter=",")
#     data = [i for i in src_r]
#     data.append(['Janna2','28','m'])
#     print(data)

# with open("data/data2.csv", "w") as file2:
#     src_w = csv.writer(file2, delimiter=",")
#     src_w.writerow(data[0])
#     for i in data[1:]:
#         src_w.writerow(i)
   
while True:



    input_text = input()



    file = open('my_file', 'w')



    file.write(input_text)