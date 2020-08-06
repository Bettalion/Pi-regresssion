import time
from matplotlib import pyplot as plt
from LR import *
Times = []
DataPoints=4 # data is DataPoints-1
TimeTemp=[]
while len(TimeTemp) <= DataPoints:
  if len(TimeTemp) == 0:
    print("Started!")
  if len(TimeTemp) == 1:
    time.sleep(1)
  if len(TimeTemp) == 2:
    time.sleep(6)
  if len(TimeTemp) == 3:
    time.sleep(3)
  if len(TimeTemp) == 3:
    time.sleep(0.9)
  TimeTemp.append(time.perf_counter())
print(TimeTemp)
for i in range(1,len(TimeTemp)):
 value = TimeTemp[i]-TimeTemp[i-1] 
 Times.append([i,int(value)])
print(Times)

m,c = LinearRegression(Times)
xp=[]
y=[]


for x in range(-5,5):
 y.append( x*m + c )
 xp.append( x )

plt.plot(xp,y)

xx , yy = sortxy(Times) 
plt.plot(xx,yy,'o')
plt.show()

