import FlipDot_Controller_Class
from time import sleep
import multiprocessing
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(processName)-10s) %(message)s',
                    )

#----Set up controller to understand PCB design and Microcontroller layout----#
onRows = [11,19,16,20,23,21,22]
offRows = [53,61,56,60,57,59,58] 
onColumns = [54,52,51,50,49,48,47,46,45,55,62,63,64,65,66,67,68,69,70,71,44,43,42,41,40,76,75,74,73,72]
offColumns = [10,12,13,14,15,8,1,2,3,9,18,17,24,31,30,29,28,27,26,25,4,5,6,7,0,36,37,38,39,32]
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

def multiPanel(scroll_text, character_offset, scroll_speed):
	#----Do Initial Clearing----#
	for FlipDot_Panel in FlipDot_Panels:
		FlipDot_Panel.flipDelay = scroll_speed
		FlipDot_Panel.allDots(1)
		FlipDot_Panel.allDots(0)

	#----Start Scroller---#
	columns_offset = 0
	columns_at_a_time = character_offset
	columns_each_character = 6
	try:
		print "Press Ctrl+C to Stop Test."
		while True:
			if __name__ == '__main__':
				message = scroll_text+" "+scroll_text
				columns_offset_total = columns_offset*columns_at_a_time
				panelnum=0
				procs=[]
				for FlipDot_Panel in FlipDot_Panels:
					c=panelnum*5
					nMessage = message[c:]
					p = multiprocessing.Process(target=flipScroller, args=(panelnum,nMessage,columns_offset_total),name=panelnum)
					procs.append(p)
					panelnum=panelnum+1
					logging.debug('starting %s', p.name)
				main_process = multiprocessing.current_process()
				for p in procs:
					if p is main_process:
						continue
					p.start()
				for p in procs:
					if p is main_process:
						continue
					p.join()
					logging.debug('joined %s', p.name)
				if columns_offset>=(len(scroll_text)*columns_each_character)/columns_at_a_time:
					columns_offset=1
				else:
					columns_offset=columns_offset+1
	except KeyboardInterrupt:
		for FlipDot_Panel in FlipDot_Panels:
			FlipDot_Panel.deInitialize
		logging.debug('cancelling %s', p.name)
		for p in procs:
			p.terminate()
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

scroll_text = raw_input("Scroll Text? ")
character_offset = int(raw_input("Character Offset? "))
scroll_speed = float(raw_input("Speed? "))
multiPanel(scroll_text, character_offset, scroll_speed)
for FlipDot_Panel in FlipDot_Panels:
	FlipDot_Panel.deInitialize
	sleep(.01)