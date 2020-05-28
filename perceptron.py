import numpy as np
import matplotlib.pyplot as plt
import pickle
import random

dbfile = open('dataset','rb')
db = np.array(pickle.load(dbfile))
w = np.array([0,0])
b = 0
count = 0

while True:
    i = random.randint(0,len(db)-1)
    x = db[i,:2]
    lab = np.dot(w.T,x) + b
    if db[i,2] * lab <= 0:
        w = w + x * db[i,2]
        count = 0
    else:
        count = count + 1
    
    if count == 10000:
        break

print(w)
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

plt.figure()
plt.plot(X_pos,Y_pos,'bo')
plt.plot(X_neg,Y_neg,'ro')
plt.plot([-2,2],[-2,2],'-k')
plt.title('orginal with x=y line as seperator')

w = w * (1/w[1])
b = b / w[1]

plt.figure()
X = np.linspace(-2,2,100)
Y = -X*w[0] - b

plt.plot(X_pos,Y_pos,'bo')
plt.plot(X_neg,Y_neg,'ro')
plt.plot(X,Y,'-k')
plt.title('seperator from perceptron ')

plt.subplots_adjust(hspace=0.5,
                    wspace=0.35)

plt.figure()
plt.plot(X_pos,Y_pos,'bo')
plt.plot(X_neg,Y_neg,'ro')
plt.plot([-2,2],[-2,2],'-c')
plt.plot(X,Y,'-k')
plt.title('both shown in one figure')


plt.show()