import json
import os
import random

print(random.randint(1000000, 99999999999999999999))

quit()

for x in os.listdir():
    if x == "Main.py":
        continue
    with open(x, "r") as f:
        Q = json.load(f)

    
    Qq = Q["Tags"]
    QQQ = Q["Scenes"]
    QQQQ = Q["Room"]

    #QQQQ.update({"ImageName": "1x3cowj49jn0p6hblb2wk55ha.jpg"})

    



    #Qq.append({"Tag": "2019","Type": 2})
    



    with open(x, "w") as f:
        json.dump(Q, f ,indent=2)