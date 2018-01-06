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

def displayScroller(scroll_text,character_offset,scroll_speed):
	FlipDot_Controller.flipDelay = scroll_speed
	FlipDot_Controller.allDots(1)
	FlipDot_Controller.allDots(0)

	columns_offset = 0
	columns_at_a_time = character_offset
	columns_each_character = 6
	try:
		print "Press Ctrl+C to Stop Test."
		while True:
			FlipDot_Controller.updateDisplay(scroll_text+" "+scroll_text,columns_offset*columns_at_a_time)
			if columns_offset>=(len(scroll_text)*columns_each_character)/columns_at_a_time:
				columns_offset=1
			else:
				columns_offset=columns_offset+1
	except KeyboardInterrupt:
		FlipDot_Controller.deInitialize
		pass

scroll_text = raw_input("Scroll Text? ")
character_offset = int(raw_input("Character Offset? "))
scroll_speed = float(raw_input("Speed? "))
displayScroller(scroll_text,character_offset,scroll_speed)
FlipDot_Controller.deInitialize()