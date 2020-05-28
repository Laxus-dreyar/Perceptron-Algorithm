import pickle
import random

dbfile = open('dataset','ab')

db = []
for i in range(100):
    pos = random.randint(0,1)
    sid = random.randint(0,1)
    l = random.uniform(-2,2)
    
    point = []
    if sid == 0:
        point = [2*(1-pos*2),l,pos]
    else:
        point = [l,-2*(1-pos*2),pos]
    
    db.append(point)

pickle.dump(db,dbfile)