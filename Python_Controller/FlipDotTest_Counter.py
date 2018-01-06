import FlipDot_Controller_Class

#----Set up controller to understand PCB design and Microcontroller layout----#
onRows = [11,19,16,20,23,21,22] 
offRows = [53,61,56,60,57,59,58] 
onColumns = [54,52,51,50,49,48,47,46,45,55,62,63,64,65,66,67,68,69,70,71,44,43,42,41,40,76,75,74,73,72] 
offColumns = [10,12,13,14,15,8,1,2,3,9,18,17,24,31,30,29,28,27,26,25,4,5,6,7,0,36,37,38,39,32] 
numOfRegisterPins = 10 * 8 
ser_Pin = 18
rclk_Pin = 23
srclk_Pin = 24

FlipDot_Controller = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 

registers=[0]*numOfRegisterPins

def displayCounter():
	FlipDot_Controller.allDots(1)
	FlipDot_Controller.allDots(0)
	t = 0
	try:
		print "Press Ctrl+C to Stop Test."
		while True:
			t=t+1
			FlipDot_Controller.updateDisplay(str(t)[:5])
	except KeyboardInterrupt:
		FlipDot_Controller.deInitialize
		pass

displayCounter()
FlipDot_Controller.deInitialize()