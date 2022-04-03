import csv,matplotlib.pyplot as plt, numpy as np
from sklearn.metrics import r2_score

x1=[]
y1=[]

x2=[]
y2=[]

x3=[]
y3=[]

dataset = []

with open('Iris.csv') as file:
    a = csv.reader(file)
    for i in a:
        if i[0] != '':
            dataset += [i] ## Accumulating Dataset
        
       
for i in dataset:
    
       ## Populating Class Arrays ##
 
        if i[5] == 'Iris-setosa':
            x1 += [float(i[4])] ## PetalLengthCm
            y1 += [float(i[3])] ## PetalWidthCm
        elif i[5] == 'Iris-versicolor':
            x2 += [float(i[4])]
            y2 += [float(i[3])]
        elif i[5] == 'Iris-virginica':
            x3 += [float(i[4])]
            y3 += [float(i[3])]
                
x1=np.array(x1)
x2=np.array(x2)
x3=np.array(x3)
y1=np.array(y1)
y2=np.array(y2)
y3=np.array(y3)

## Splitting Training Data ##

x1, x2, x3 = x1[:30], x2[:30], x3[:30]
y1, y2, y3 = y1[:30], y2[:30], y3[:30] 


## Plotting Training Data ##

plt.scatter(x1,y1,color='green')
plt.scatter(x2,y2,color='black')
plt.scatter(x3,y3,color='orange')
plt.tight_layout()  


## Compiling all 3 classes to obtain entire dataset (training) ##

x = np.concatenate((x1,x2,x3))
y = np.concatenate((y1,y2,y3))

## Creating testing parameters ##

test_predicted=[]
test_check=[]
test_x =[]
test_y = []

for i in dataset:
    if i[0]!="":
        test_x += [float(i[4])]
        test_y += [float(i[3])]
        if i[5]=='Iris-setosa':
            test_check+=[1]
        elif i[5] == 'Iris-versicolor':
            test_check+=[2]
        elif i[5] == 'Iris-virginica':
            test_check+=[3]

test_check = test_check[30:50] + test_check[80:100] + test_check[130:150]
test_x = test_x[30:50] + test_x[80:100] + test_x[130:150]
test_y = test_y[30:50] + test_y[80:100] + test_y[130:150]

for i in range(len(test_x)):
    
    x_means = np.array([np.mean(x1),np.mean(x2),np.mean(x3)])
    y_means = np.array([np.mean(y1),np.mean(y2),np.mean(y3)])

    dist=[]

    dist = np.sqrt(np.square(test_x[i]-x_means)+np.square(test_y[i]-y_means))

    index = np.where(dist == min(dist))[0]

    if index==0: 
        test_predicted+=[1]
    elif index==1: 
        test_predicted+=[2]
    elif index==2:
        test_predicted+=[3]
    

accuracy = 0
for i in range(60):
    if test_predicted[i]==test_check[i]:
        accuracy+=1
    
accuracy = (accuracy/60)*100

print(r2_score(test_check,test_predicted),accuracy)