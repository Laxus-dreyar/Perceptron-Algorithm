import numpy as np
import matplotlib.pyplot as plt
import pickle

dbfile = open('dataset','rb')
db = np.array(pickle.load(dbfile))

w = np.array([0,0])
b = 0

for i in len(db):
    x = db[i,:2]
    lab = np.dot(w.T,x) + b
    if db