import numpy as np, matplotlib.pyplot as plt, random

import csv

# x=[]
# y=[]
# z=[]
# with open("SOCR-HeightWeight.csv",'r') as file:
#     a = csv.reader(file)
#     for i in a:
#         z+=[i[0].split(',')]
#         # x+=[float(z[1])]
#         # y+=[float(z[2])]

# n= 40
# for i in range(2,n):
#     a,b = float(z[i][1]),float(z[i][2])
#     x+=[a]
#     y+=[b]

n = 30
a,b = random.randrange(0,50),random.randrange(50,80)
x = np.random.randint(a,b,n)
a,b = random.randrange(0,50),random.randrange(50,80)
y = np.random.randint(a,b,n)

x.sort()
y.sort()

plt.xlim([0,100])
plt.ylim([0,100])
plt.scatter(x,y)

one = np.ones(n)
Y = np.transpose(y)

A = np.column_stack((np.transpose(x),one))
A1 = np.transpose(A)

X = np.dot(np.linalg.inv(np.dot(A1,A)),np.dot(A1,y))

yi = np.multiply(X[0],x) + X[1]

e = sum(np.square(np.subtract(yi,y)))


plt.plot(x,yi)