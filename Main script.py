from matplotlib import pyplot as plt
import RPi.GPIO as GPIO
import time
from LR import *

ButP = 10
PresP = 16
StaP = 18

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) #set mode

GPIO.setup(PresP, GPIO.OUT)
GPIO.setup(StaP, GPIO.OUT)
GPIO.setup(ButP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(StaP,GPIO.HIGH) # start led pin on

MainData =[] # main data / times

LightInt = 0.5

DataPoints=6 
TimeTemp=[]
while len(TimeTemp) <= DataPoints:
 if GPIO.input(ButP) == GPIO.HIGH: # if button pressed then:
  if len(TimeTemp) == 0:
    print("Started!")

  GPIO.output(PresP,GPIO.HIGH) # pressed led pin on
  time.sleep(LightInt)           #light iterval
  GPIO.output(StaP,GPIO.LOW) # pressed led pin off

  TimeTemp.append(time.perf_counter()-LightInt)
  

for i in range(1,len(TimeTemp)):
 TimeE = TimeTemp[i]-TimeTemp[i-1] #time elapsed
 MainData.append(int(TimeE)) 
print(MainData)

GPIO.output(StaP,GPIO.LOW) # start led pin off
print('Done!')

 
m,c = LinearRegression(MainData)

px=[]
py=[]
rx, ry = sortxy(MainData)
for r in range(-5,len(MainData)+5):
  px.append(r)
  py.append( (m * r) + c )

plt.plot(rx,ry,'o')
plt.plot(px,py)
plt.show()

GPIO.cleanup()