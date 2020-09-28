import FlipDot_Controller_Class2 as FlipDot_Controller_Class
import datetime
import time

#----Set up controller to understand PCB design and Microcontroller layout----#

#!use the class

offRows=[5,7,3,2,1,4,6]
onRows=[44,47,42,40,46,41,43]#69#27
offColumns = [74,48,73,49,50, 72,71,51,70,52, 53,69,54,68,55, 67,56,66,57,58, 59,65,60,64,61]
onColumns = [38,8,39,15,14, 32,25,13,26,12, 11,27,10,28,9, 29,16,30,23,22, 21,31,20,24,19]

numOfRegisterPins = 10 * 8
ser_Pin = 18
rclk_Pin = 23
srclk_Pin = 24

FlipDot_Controller = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 

registers=[0]*numOfRegisterPins

def onOffTest():
    try:
        for x in range(100):
            FlipDot_Controller.allDots(1)
            #time.sleep(.02)
            FlipDot_Controller.allDots(0)
            #time.sleep(.02)
    except KeyboardInterrupt:
        FlipDot_Controller.deInitialize
        pass
    
def displayTime():
    FlipDot_Controller.allDots(1)
    FlipDot_Controller.allDots(0)
    t = "time"
    try:
        print("Press Ctrl+C to Stop Test.")
        c=0
        while True:
            c=c+1
            datetime.datetime.now().time()
            #if t != datetime.datetime.now().strftime("%I:%M"):
            #    t = datetime.datetime.now().strftime("%I:%M")
            #time.sleep(.1) #can go as low as .01 - but check power rain
            FlipDot_Controller.updateDisplay(str(c))
    except KeyboardInterrupt:
        FlipDot_Controller.deInitialize
        pass

displayTime()
#onOffTest()
FlipDot_Controller.deInitialize()



#need to update pin 9 - needs to connect to a different shift register
