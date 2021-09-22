import os
import datetime
from playsound import playsound
os.system('cls')
timeH=int(input("Hour in which alarm will ring : "))
timeM=int(input("Minute in which alarm will ring : "))

amPm=str(input("am or pm : "))
os.system('cls')
print("Waiting for alarm : ",timeH,timeM,amPm)
if(amPm=='pm'):
    amPm=amPm+12

while(True):
    if(timeH==datetime.datetime.now().hour and timeM==datetime.datetime.now().minute):
        print("time to wake Up")
        playsound('alarm2.mp3')
    