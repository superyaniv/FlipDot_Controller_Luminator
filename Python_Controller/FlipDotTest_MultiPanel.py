import FlipDot_Controller_Class
from time import sleep
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

#----Set up controller to understand PCB design and Microcontroller layout----#
onRows = [0,1,2,3,4,5,6] #[53,61,56,60,57,59,58]
offRows = [8,9,10,11,12,13,14] #[53,61,56,60,57,59,58]
onColumns = [31,30,29,28,27,24,25,26,72,40,41,42,43,44,45,46,47,56,57,58,73,74,75,76,77,63,62,61,60,59] #[54,52,51,50,49,48,47,46,45,55,62,63,64,65,66,67,68,69,70,71,44,43,42,41,40,76,75,74,73,72]
offColumns = [23,22,21,20,19,16,17,18,64,32,33,34,35,36,37,38,39,48,49,50,65,66,67,68,69,55,54,53,52,51] #[10,12,13,14,15,8,1,2,3,9,18,17,24,31,30,29,28,27,26,25,4,5,6,7,0,36,37,38,39,32]
numOfRegisterPins = 10 * 8 
FlipDot_Panels = []

#----Panel #1----#
ser_Pin = 18
rclk_Pin = 23
srclk_Pin = 24
FlipDot_Panels[1] = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 
#----Panel #2----#
#ser_Pin = 18
#rclk_Pin = 23
#srclk_Pin = 24
#FlipDot_Panels[2] = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 
#----Panel #3----#
#ser_Pin = 18
#rclk_Pin = 23
#srclk_Pin = 24
#FlipDot_Panels[3] = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 


registers=[0]*numOfRegisterPins

def displayScroller():
	FlipDot_Controller.allDots(0)
	t = "KELEIGH SUCKS! "
	columns_offset = 0
	columns_at_a_time = 6
	columns_each_character = 6
	try:
		print "Press Ctrl+C to Stop Test."
		while True:
			for panel in FlipDot_Panels:
				t = threading.Thread(target=worker, kwrgs={'panelDisplay':t+t,'columns_offset_total':columns_offset*columns_at_a_time})
				#FlipDot_Panels[panel].updateDisplay(t+t,columns_offset*columns_at_a_time)
			for t in threading.enumerate():
				if t is main_thread:
					continue
				logging.debug('joining %s', t.getName())
				t.join()
			if columns_offset>=(len(t)*columns_each_character)/columns_at_a_time:
				columns_offset=1
			else:
				columns_offset=columns_offset+1
	except KeyboardInterrupt:
		FlipDot_Controller.deInitialize
		logging.debug('joining %s', t.getName())
		t.join()
		pass

def worker(panelDisplay,columns_offset_total):
	FlipDot_Panels[panel].updateDisplay(panelDisplay,columns_offset_total)


displayScroller()
FlipDot_Controller.deInitialize()