import numpy as np
import matplotlib.pyplot as plt
import pickle

dbfile = open('dataset','rb')
db = np.array(pickle.load(dbfile))

X = db[:,:1]
Y = db[:,1:2]
label = db[:,2:3]

X_pos = []
Y_pos = []
X_neg = []
Y_neg = []

for i in range(len(X)):
    if label[i] == 1:
        X_pos.append(X[i])
        Y_pos.append(Y[i])
    else:
        X_neg.append(X[i])
        Y_neg.append(Y[i])

plt.plot(X_pos,Y_pos,'bo')
plt.plot(X_neg,Y_neg,'ro')
plt.plot([-2,2],[-2,2],'-k')
plt.show()