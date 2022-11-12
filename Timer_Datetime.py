# import json


# with open("data.json", 'w') as file:
#     tx = json.dumps(file)



# import sqlite3

# products = json.load(("data.json").read_text)

# with sqlite3.connect("test_db.sqlite3") as connect:
#     cur = connect.cursor() 


from datetime import datetime, timedelta

time = timedelta(days=110, hours=254)

tm = datetime.now()

print(tm.strftime("%Y"))


t = 1523443804

l = datetime.fromtimestamp(t)
print(l)

import time

while True:
    date = time.localtime()
    print(time.strftime("%H:%M:%S", date))
    time.sleep(1)