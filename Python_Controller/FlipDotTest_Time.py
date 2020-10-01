import FlipDot_Controller_Class
import datetime
import time

#----Set up controller to understand PCB design and Microcontroller layout----#

onRows = [7,5,0,3,2,6,4]
offRows = [42,40,44,41,43,46,45]
onColumns = [48,74,49,73,50,72,51,71,52,70,53,69,54,68,55,56,67,57,66,58,59,60,65,61,64]
offColumns = [8,38,15,39,14,32,13,25,12,26,11,27,10,28,9,16,29,23,30,22,21,20,31,19,24]

numOfRegisterPins = 10 * 8
ser_Pin = 25
rclk_Pin = 24
srclk_Pin = 23

FlipDot_Controller = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 

registers=[0]*numOfRegisterPins

def displayTime():
	FlipDot_Controller.allDots(1)
	FlipDot_Controller.allDots(0)
	t = "time"
	try:
		print "Press Ctrl+C to Stop Test."
		while True:

			datetime.datetime.now().time()
			if t != datetime.datetime.now().strftime("%I:%M"):
				t = datetime.datetime.now().strftime("%I:%M")
			time.sleep(1)
			FlipDot_Controller.updateDisplay(t)
	except KeyboardInterrupt:
		FlipDot_Controller.deInitialize
		pass

displayTime()
FlipDot_Controller.deInitialize()
