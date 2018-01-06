import FlipDot_Controller_Class
from time import sleep
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

#----Set up controller to understand PCB design and Microcontroller layout----#
onRows = [11,19,16,20,23,21,22] #[0,1,2,3,4,5,6] #[11,19,16,20,23,21,22]
offRows = [53,61,56,60,57,59,58] #[8,9,10,11,12,13,14]
onColumns = [54,52,51,50,49,48,47,46,45,55,62,63,64,65,66,67,68,69,70,71,44,43,42,41,40,76,75,74,73,72] #[31,30,29,28,27,24,25,26,72,40,41,42,43,44,45,46,47,56,57,58,73,74,75,76,77,63,62,61,60,59]
offColumns = [10,12,13,14,15,8,1,2,3,9,18,17,24,31,30,29,28,27,26,25,4,5,6,7,0,36,37,38,39,32] #[23,22,21,20,19,16,17,18,64,32,33,34,35,36,37,38,39,48,49,50,65,66,67,68,69,55,54,53,52,51]
numOfRegisterPins = 10 * 8 
FlipDot_Panels = [0 for i in range(3)]

#----Panel #1----#
ser_Pin = 18
rclk_Pin = 23
srclk_Pin = 24
FlipDot_Panels[0] = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 
#----Panel #2----#
ser_Pin = 17
rclk_Pin = 27
srclk_Pin = 22
FlipDot_Panels[1] = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 
#----Panel #3----#
ser_Pin = 5
rclk_Pin = 6
srclk_Pin = 13
FlipDot_Panels[2] = FlipDot_Controller_Class.FlipDot_Controller_Class(1, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin) 

def multiPanel():
	#----Do Initial Clearing----#
	for FlipDot_Panel in FlipDot_Panels:
		t = threading.Thread(target=onOffer, kwargs={'panelNumber':n})
		#FlipDot_Panel.allDots(1)
		#FlipDot_Panel.allDots(0)
	for t in threading.enumerate():
		if t is main_thread:
			continue
		t.join()
		logging.debug('joined %s', t.getName())

	#----Start Scroller---#
	displayText = "KELEIGH SUCKS! "
	columns_offset = 0
	columns_at_a_time = 6
	columns_each_character = 6
	try:
		print "Press Ctrl+C to Stop Test."
		while True:
			message = displayText+displayText
			columns_offset_total = columns_offset*columns_at_a_time
			n=0
			for FlipDot_Panel in FlipDot_Panels:
				c=n*5
				nMessage = message[c:]
				t = threading.Thread(target=flipScroller, kwargs={'panelNumber':n,'panelDisplay':nMessage,'columns_offset_total':columns_offset_total})
				n=n+1
				logging.debug('starting %s', t.getName())
				t.start()
			main_thread = threading.currentThread()
			for t in threading.enumerate():
				if t is main_thread:
					continue
				t.join()
				logging.debug('joined %s', t.getName())
			if columns_offset>=(len(displayText)*columns_each_character)/columns_at_a_time:
				columns_offset=1
			else:
				columns_offset=columns_offset+1
	except KeyboardInterrupt:
		for FlipDot_Panel in FlipDot_Panels:
			FlipDot_Panel.deInitialize
		#logging.debug('cancelling %s', t.getName())
		#t.cancel()
		pass

def flipScroller(panelNumber,panelDisplay,columns_offset_total):
	logging.debug('Starting Panel #:'+str(panelNumber))
	FlipDot_Panels[panelNumber].updateDisplay(panelDisplay,columns_offset_total)
	logging.debug('Exiting Panel #:'+str(panelNumber))
	return

def onOffer(panelNumber):
	logging.debug('Starting Panel #:'+str(panelNumber))
	FlipDot_Panels[panelNumber].allDots(1)
	FlipDot_Panels[panelNumber].allDots(0)
	logging.debug('Exiting Panel #:'+str(panelNumber))
	return

multiPanel()
for FlipDot_Panel in FlipDot_Panels:
	FlipDot_Panel.deInitialize
	sleep(.01)