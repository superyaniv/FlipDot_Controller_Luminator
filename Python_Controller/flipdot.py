import wiringpi2 as wiringpi  
import datetime
from time import sleep
from twitter import *
import requests, json

SER_Pin = 18;   #pin 14 on the 75HC595
RCLK_Pin = 23;  #pin 12 on the 75HC595
SRCLK_Pin = 24; #pin 11 on the 75HC595
numOfRegisterPins = 10 * 8

registers=[0]*numOfRegisterPins

onRows = [0,1,2,3,4,5,6];
offRows = [8,9,10,11,12,13,14];
onColumns = [31,30,29,28,27,24,25,26,72,40,41,42,43,44,45,46,47,56,57,58,73,74,75,76,77,63,62,61,60,59];
offColumns= [23,22,21,20,19,16,17,18,64,32,33,34,35,36,37,38,39,48,49,50,65,66,67,68,69,55,54,53,52,51];

oldnew_onRows = [64,58,63,59,62,60,61]
oldnew_offRows = [17,23,18,22,19,21,20]
oldnew_onColumns = [49,69,50,68,51,56,55,54,53,70,48,71,47,72,46,73,45,74,44,75,64,65,66,52,67,41,77,42,76,43]
oldnew_offColumns = [9,29,16,30,11,10,11,12,13,28,2,27,3,26,4,33,5,40,6,2,9,14,31,14,30,1,37,8,38,7]

newnew_onRows = [53,61,56,60,57,59,58]
newnew_offRows = [11,19,16,20,23,21,22]
newnew_onColumns = [54,52,51,50,49,48,47,46,45,55,62,63,64,65,66,67,68,69,70,71,44,43,42,41,40,76,75,74,73,72]
newnew_offColumns = [10,12,13,14,15,8,1,2,3,9,18,17,24,31,30,29,28,27,26,25,4,5,6,7,0,36,37,38,39,32]

alphabet = [[0x00,0x00,0x00,0x00,0x00],[0x00,0x00,0x6f,0x00,0x00],[0x00,0x07,0x00,0x07,0x00],[0x14,0x7f,0x14,0x7f,0x14],[0x00,0x07,0x04,0x1e,0x00],[0x23,0x13,0x08,0x64,0x62],[0x36,0x49,0x56,0x20,0x50],[0x00,0x00,0x07,0x00,0x00],[0x00,0x1c,0x22,0x41,0x00],[0x00,0x41,0x22,0x1c,0x00],[0x14,0x08,0x3e,0x08,0x14],[0x08,0x08,0x3e,0x08,0x08],[0x00,0x50,0x30,0x00,0x00],[0x08,0x08,0x08,0x08,0x08],[0x00,0x60,0x60,0x00,0x00],[0x20,0x10,0x08,0x04,0x02],[0x3e,0x51,0x49,0x45,0x3e],[0x00,0x42,0x7f,0x40,0x00],[0x42,0x61,0x51,0x49,0x46],[0x21,0x41,0x45,0x4b,0x31],[0x18,0x14,0x12,0x7f,0x10],[0x27,0x45,0x45,0x45,0x39],[0x3c,0x4a,0x49,0x49,0x30],[0x01,0x71,0x09,0x05,0x03],[0x36,0x49,0x49,0x49,0x36],[0x06,0x49,0x49,0x29,0x1e],[0x00,0x36,0x36,0x00,0x00],[0x00,0x56,0x36,0x00,0x00],[0x08,0x14,0x22,0x41,0x00],[0x14,0x14,0x14,0x14,0x14],[0x00,0x41,0x22,0x14,0x08],[0x02,0x01,0x51,0x09,0x06],[0x3e,0x41,0x5d,0x49,0x4e],[0x7e,0x09,0x09,0x09,0x7e],[0x7f,0x49,0x49,0x49,0x36],[0x3e,0x41,0x41,0x41,0x22],[0x7f,0x41,0x41,0x41,0x3e],[0x7f,0x49,0x49,0x49,0x41],[0x7f,0x09,0x09,0x09,0x01],[0x3e,0x41,0x49,0x49,0x7a],[0x7f,0x08,0x08,0x08,0x7f],[0x00,0x41,0x7f,0x41,0x00],[0x20,0x40,0x41,0x3f,0x01],[0x7f,0x08,0x14,0x22,0x41],[0x7f,0x40,0x40,0x40,0x40],[0x7f,0x02,0x0c,0x02,0x7f],[0x7f,0x04,0x08,0x10,0x7f],[0x3e,0x41,0x41,0x41,0x3e],[0x7f,0x09,0x09,0x09,0x06],[0x3e,0x41,0x51,0x21,0x5e],[0x7f,0x09,0x19,0x29,0x46],[0x46,0x49,0x49,0x49,0x31],[0x01,0x01,0x7f,0x01,0x01],[0x3f,0x40,0x40,0x40,0x3f],[0x0f,0x30,0x40,0x30,0x0f],[0x3f,0x40,0x30,0x40,0x3f],[0x63,0x14,0x08,0x14,0x63],[0x07,0x08,0x70,0x08,0x07],[0x61,0x51,0x49,0x45,0x43],[0x3c,0x4a,0x49,0x29,0x1e],[0x02,0x04,0x08,0x10,0x20],[0x00,0x41,0x7f,0x00,0x00],[0x04,0x02,0x01,0x02,0x04],[0x40,0x40,0x40,0x40,0x40],[0x00,0x00,0x03,0x04,0x00],[0x20,0x54,0x54,0x54,0x78],[0x7f,0x48,0x44,0x44,0x38],[0x38,0x44,0x44,0x44,0x20],[0x38,0x44,0x44,0x48,0x7f],[0x38,0x54,0x54,0x54,0x18],[0x08,0x7e,0x09,0x01,0x02],[0x0c,0x52,0x52,0x52,0x3e],[0x7f,0x08,0x04,0x04,0x78],[0x00,0x44,0x7d,0x40,0x00],[0x20,0x40,0x44,0x3d,0x00],[0x00,0x7f,0x10,0x28,0x44],[0x00,0x41,0x7f,0x40,0x00],[0x7c,0x04,0x18,0x04,0x78],[0x7c,0x08,0x04,0x04,0x78],[0x38,0x44,0x44,0x44,0x38],[0x7c,0x14,0x14,0x14,0x08],[0x08,0x14,0x14,0x18,0x7c],[0x7c,0x08,0x04,0x04,0x08],[0x48,0x54,0x54,0x54,0x20],[0x04,0x3f,0x44,0x40,0x20],[0x3c,0x40,0x40,0x20,0x7c],[0x1c,0x20,0x40,0x20,0x1c],[0x3c,0x40,0x30,0x40,0x3c],[0x44,0x28,0x10,0x28,0x44],[0x0c,0x50,0x50,0x50,0x3c],[0x44,0x64,0x54,0x4c,0x44],[0x00,0x08,0x36,0x41,0x41],[0x00,0x00,0x7f,0x00,0x00],[0x41,0x41,0x36,0x08,0x00],[0x04,0x02,0x04,0x08,0x04],]
#alphabet = [[0,0,0,0,0],[0,56,125,56,0],[80,96,0,80,96],[20,127,20,127,20],[18,42,127,42,36],[98,100,8,19,35],[54,73,85,34,5],[0,80,96,0,0], [0,28,34,65,0],[0,65,34,28,0],[20,8,62,8,20],[8,8,62,8,8],[0,5,6,0,0],[8,8,8,8,8],[0,3,3,0,0],[2,4,8,16,32],[62,69,73,81,62],[17,33,127,1,1],[33,67,69,73,49],[34,65,73,73,54],[12,20,36,127,4],[114,81,81,81,78],[62,73,73,73,38],[64,71,72,80,96],[54,73,73,73,54],[50,73,73,73,62],[0,54,54,0,0],[0,53,54,0,0],[8,20,34,65,0],[20,20,20,20,20],[0,65,34,20,8],[32,64,69,72,48],[62,73,87,85,62],[31, 36, 68, 36, 31],[127, 73, 73, 73, 54],[62, 65, 65, 65, 34],[127, 65, 65, 34, 28],[127, 73, 73, 65, 65],[127, 72, 72, 72, 64],[62, 65, 65, 69, 38],[127, 8, 8, 8, 127],[0, 65, 127, 65, 0],[2, 1, 1, 1, 126],[127, 8, 20, 34, 65],[127, 1, 1, 1, 1],[127, 32, 16, 32, 127],[127, 32, 16, 8, 127],[62, 65, 65, 65, 62],[127, 72, 72, 72, 48],[62, 65, 69, 66, 61],[127, 72, 76, 74, 49],[50, 73, 73, 73, 38],[64, 64, 127, 64, 64],[126, 1, 1, 1, 126],[124, 2, 1, 2, 124],[126, 1, 6, 1, 126],[99, 20, 8, 20, 99],[96, 16, 15, 16, 96],[67, 69, 73, 81, 97],[0,127,65,65,0],[32,16,8,4,2],[0,65,65,127,0],[16,32,64,32,16],[1,1,1,1,1],[0,64,32,16,0],[2,21,21,14,1],[64,126,9,17,14],[14,17,17,17,10],[14,17,74,127,1],[14,21,21,21,9],[1,9,63,72,32],[9,21,21,21,30],[127,8,8,8,7],[0,0,46,1,1],[2,1,1,1,94],[1,127,4,10,17],[0,65,127,1,0],[31,16,14,16,31],[31,8,16,16,15],[14,17,17,17,14],[127,20,20,20,8],[8,20,20,31,1],[31,8,16,16,8],[9,21,21,21,18],[16,16,126,17,18],[30,1,1,30,1],[28,2,1,2,28],[30,1,6,1,30],[17,10,4,10,17],[16,9,6,8,16],[17,19,21,25,17],[8,54,65,65,0],[0,0,127,0,0],[0,65,65,54,8],[32,64,32,16,32]]
wiringpi.wiringPiSetupGpio()  
wiringpi.pinMode(24, 1)      # sets GPIO 24 to output  
wiringpi.pinMode(23, 1)
wiringpi.pinMode(18, 1)


def writeRegisters():
	wiringpi.digitalWrite(RCLK_Pin, 0)
	for i in range(numOfRegisterPins-1,-1,-1):
		wiringpi.digitalWrite(SRCLK_Pin, 0)
		val = registers[i]
#		print "setting register "+str(i)+" as "+str(val)
		wiringpi.digitalWrite(SER_Pin, val)
		wiringpi.digitalWrite(SRCLK_Pin, 1)
	wiringpi.digitalWrite(RCLK_Pin, 1)

def clearRegisters():
#        print ".....Clearing Register Pins....."
	for i in range(0,numOfRegisterPins):
		registers[i] = 0

def setRegisterPin(p,val):
#	print ".....Setting Register Pins....."
        for i in range(0,numOfRegisterPins):
		if i == p:
			registers[i] = val
		else:
			registers[i] = 0

def flipDot(col,row,onFlip,d):
	if onFlip:
		flipDotPin(onColumns[col],onRows[row],d)
	else:
		flipDotPin(offColumns[col],offRows[row],d)

def flipDotPin(pin1,pin2,d):
	for p in range(0,numOfRegisterPins):
		if p==pin1 or p==pin2:
			registers[p]=1
		else:
			registers[p]=0
	writeRegisters()
	sleep(d)
	clearRegisters()
	writeRegisters()

def clearDots():
	for r in range(0,7):
        	for c in range(0,30):
                	flipDot(c,r,0,.01)

def allDotsOn():
	for r in range(0,7):
		for c in range(0,30):
			flipDot(c,r,1,.01)

def allDotsOnMult():
	for c in range(0,30):
		flipDotPinMult(onColumns[c],onRows[0])
		flipDotPinMult(onColumns[c],onRows[1])
		flipDotPinMult(onColumns[c],onRows[2])
		flipDotPinMult(onColumns[c],onRows[3])
		flipDotPinMult(onColumns[c],onRows[4])
		flipDotPinMult(onColumns[c],onRows[5])
		flipDotPinMult(onColumns[c],onRows[6])
		sleep(.01)
		clearRegisters()
		writeRegisters()

def flipDotPinMult(pin1,pin2):
        for p in range(0,numOfRegisterPins):
                if p==pin1 or p==pin2:
                        registers[p]=1
                else:
                        registers[p]=0
        writeRegisters()



def updateDisplay(textMessage):
	alphabetIndex=[]
	currentColumn = 0
	displaysize = 5
	for ch in range(0,displaysize):
		alphabetIndex.append(ord(textMessage[ch])-32)
		if alphabetIndex <0: 
			alphabetIndex=0

	for segment in range(0,5):
		for col in range(0,5):
			columnbins= alphabet[alphabetIndex[segment]]
			if col <= 5: 
				x = bin(columnbins[col])
			
			z = [bool(int(y)) for y in x[2:]]
                	for f in range(0,7-len(z)):
                        	z=[0]+z			
			r=0
			for isOn in z:
				flipDot(segment*6+col,r,isOn,.005)
				r=r+1

def twitterDisplay():

	#-----set up twitter-----#
	config = {}
	execfile("config.py", config)
	twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
	results = twitter.trends.place(_id = 2487889)
	#San Diego: 2487889
	#united Sates: 23424977

	for location in results:
		r=0
        	for trend in location["trends"]:
			updateDisplay(trend["name"])
			print trend["name"]
			sleep(1)

def displayTime():
	#--display time--#
	t = "time"
	try:
	    	while True:
			now = datetime.datetime.now().time()
			if t != now.strftime("%M:%S"):
				t = now.strftime("%M:%S")
				updateDisplay(t)
	except KeyboardInterrupt:
		clearRegisters()
		writeRegisters()
		wiringpi.digitalWrite(SER_Pin, 0)
		wiringpi.digitalWrite(RCLK_Pin, 0)
		wiringpi.digitalWrite(SRCLK_Pin, 0)
		pass

def displayBitcoin():
        #--display bitcoin price--#
	btcprice = "btc"
        try:
                while True:
			ubtcprice = str(round(getBitcoinPrice(),0))[:3]
			print ubtcprice
                        if btcprice != ubtcprice:
                                btcprice = ubtcprice
				updateDisplay(" "+btcprice+" ")
			sleep(30)
        except KeyboardInterrupt:
                clearRegisters()
                writeRegisters()
                wiringpi.digitalWrite(SER_Pin, 0)
                wiringpi.digitalWrite(RCLK_Pin, 0)
                wiringpi.digitalWrite(SRCLK_Pin, 0)
                pass
	except:
		pass


def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print "Error querying Bitstamp API"

def displayOnOffTest():
	try:
		while True:
			clearDots()
			allDotsOn()
			#allDotsOnMult()
			#sleep(1)
	except KeyboardInterrupt:
		clearRegisters()
		writeRegisters()
                wiringpi.digitalWrite(SER_Pin, 0)
                wiringpi.digitalWrite(RCLK_Pin, 0)
                wiringpi.digitalWrite(SRCLK_Pin, 0)
		pass
	except: 
		pass

def testtest():
	allDotsOnMult()

def newBoardTest():
	#turn on r14c3
	clearRegisters()
	writeRegisters()
	pin1 = 20
	pin2 = 50
        for p in range(0,79):
                if p==pin1 or p==pin2:
                        registers[p]=1
                else:
                        registers[p]=0
        writeRegisters()
        sleep(5)
        clearRegisters()
        writeRegisters()

def newBoardTestFlip():
	flipDot(1,1,1,2)
	flipDot(1,1,0,2)


clearRegisters()
writeRegisters()
#twitterDisplay()
#displayTime()
#displayBitcoin()
displayOnOffTest()
#testtest()
#newBoardTest()
#newBoardTestFlip()

wiringpi.digitalWrite(SER_Pin, 0)
wiringpi.digitalWrite(RCLK_Pin, 0)
wiringpi.digitalWrite(SRCLK_Pin, 0)
