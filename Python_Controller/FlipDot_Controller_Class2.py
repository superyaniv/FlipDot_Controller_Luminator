import RPi.GPIO as IO
from time import sleep

class FlipDot_Controller_Class:

    alphabet = [[0x00,0x00,0x00,0x00,0x00],[0x00,0x00,0x6f,0x00,0x00],[0x00,0x07,0x00,0x07,0x00],[0x14,0x7f,0x14,0x7f,0x14],[0x00,0x07,0x04,0x1e,0x00],[0x23,0x13,0x08,0x64,0x62],[0x36,0x49,0x56,0x20,0x50],[0x00,0x00,0x07,0x00,0x00],[0x00,0x1c,0x22,0x41,0x00],[0x00,0x41,0x22,0x1c,0x00],[0x14,0x08,0x3e,0x08,0x14],[0x08,0x08,0x3e,0x08,0x08],[0x00,0x50,0x30,0x00,0x00],[0x08,0x08,0x08,0x08,0x08],[0x00,0x60,0x60,0x00,0x00],[0x20,0x10,0x08,0x04,0x02],[0x3e,0x51,0x49,0x45,0x3e],[0x00,0x42,0x7f,0x40,0x00],[0x42,0x61,0x51,0x49,0x46],[0x21,0x41,0x45,0x4b,0x31],[0x18,0x14,0x12,0x7f,0x10],[0x27,0x45,0x45,0x45,0x39],[0x3c,0x4a,0x49,0x49,0x30],[0x01,0x71,0x09,0x05,0x03],[0x36,0x49,0x49,0x49,0x36],[0x06,0x49,0x49,0x29,0x1e],[0x00,0x36,0x36,0x00,0x00],[0x00,0x56,0x36,0x00,0x00],[0x08,0x14,0x22,0x41,0x00],[0x14,0x14,0x14,0x14,0x14],[0x00,0x41,0x22,0x14,0x08],[0x02,0x01,0x51,0x09,0x06],[0x3e,0x41,0x5d,0x49,0x4e],[0x7e,0x09,0x09,0x09,0x7e],[0x7f,0x49,0x49,0x49,0x36],[0x3e,0x41,0x41,0x41,0x22],[0x7f,0x41,0x41,0x41,0x3e],[0x7f,0x49,0x49,0x49,0x41],[0x7f,0x09,0x09,0x09,0x01],[0x3e,0x41,0x49,0x49,0x7a],[0x7f,0x08,0x08,0x08,0x7f],[0x00,0x41,0x7f,0x41,0x00],[0x20,0x40,0x41,0x3f,0x01],[0x7f,0x08,0x14,0x22,0x41],[0x7f,0x40,0x40,0x40,0x40],[0x7f,0x02,0x0c,0x02,0x7f],[0x7f,0x04,0x08,0x10,0x7f],[0x3e,0x41,0x41,0x41,0x3e],[0x7f,0x09,0x09,0x09,0x06],[0x3e,0x41,0x51,0x21,0x5e],[0x7f,0x09,0x19,0x29,0x46],[0x46,0x49,0x49,0x49,0x31],[0x01,0x01,0x7f,0x01,0x01],[0x3f,0x40,0x40,0x40,0x3f],[0x0f,0x30,0x40,0x30,0x0f],[0x3f,0x40,0x30,0x40,0x3f],[0x63,0x14,0x08,0x14,0x63],[0x07,0x08,0x70,0x08,0x07],[0x61,0x51,0x49,0x45,0x43],[0x3c,0x4a,0x49,0x29,0x1e],[0x02,0x04,0x08,0x10,0x20],[0x00,0x41,0x7f,0x00,0x00],[0x04,0x02,0x01,0x02,0x04],[0x40,0x40,0x40,0x40,0x40],[0x00,0x00,0x03,0x04,0x00],[0x20,0x54,0x54,0x54,0x78],[0x7f,0x48,0x44,0x44,0x38],[0x38,0x44,0x44,0x44,0x20],[0x38,0x44,0x44,0x48,0x7f],[0x38,0x54,0x54,0x54,0x18],[0x08,0x7e,0x09,0x01,0x02],[0x0c,0x52,0x52,0x52,0x3e],[0x7f,0x08,0x04,0x04,0x78],[0x00,0x44,0x7d,0x40,0x00],[0x20,0x40,0x44,0x3d,0x00],[0x00,0x7f,0x10,0x28,0x44],[0x00,0x41,0x7f,0x40,0x00],[0x7c,0x04,0x18,0x04,0x78],[0x7c,0x08,0x04,0x04,0x78],[0x38,0x44,0x44,0x44,0x38],[0x7c,0x14,0x14,0x14,0x08],[0x08,0x14,0x14,0x18,0x7c],[0x7c,0x08,0x04,0x04,0x08],[0x48,0x54,0x54,0x54,0x20],[0x04,0x3f,0x44,0x40,0x20],[0x3c,0x40,0x40,0x20,0x7c],[0x1c,0x20,0x40,0x20,0x1c],[0x3c,0x40,0x30,0x40,0x3c],[0x44,0x28,0x10,0x28,0x44],[0x0c,0x50,0x50,0x50,0x3c],[0x44,0x64,0x54,0x4c,0x44],[0x00,0x08,0x36,0x41,0x41],[0x00,0x00,0x7f,0x00,0x00],[0x41,0x41,0x36,0x08,0x00],[0x04,0x02,0x04,0x08,0x04]]
    columns_per_Segment = 5
    displayColumns = 25
    displayRows = 7

    def __init__(self, name, onRows, offRows, onColumns, offColumns, numOfRegisterPins, ser_Pin, rclk_Pin, srclk_Pin):
        self.name = name    # Name of the controller or panel
        self.onRows = onRows    # OnRow pins
        self.offRows = offRows
        self.onColumns = onColumns
        self.offColumns = offColumns
        self.numOfRegisterPins = numOfRegisterPins
        self.ser_Pin = ser_Pin
        self.rclk_Pin = rclk_Pin
        self.srclk_Pin = srclk_Pin
        self.initializePI()
        self.registers= [0] * numOfRegisterPins
        self.oldDisplayState = [[0 for s in range(self.displayRows)] for c in range(self.displayColumns)]
        self.flipDelay = .015 #timing1

    def initializePI(self):
        IO.setmode(IO.BCM)
        IO.setup(self.ser_Pin,IO.OUT)
        IO.setup(self.rclk_Pin,IO.OUT)
        IO.setup(self.srclk_Pin,IO.OUT)

    def choose_Alphabet(self, newAlphabet):
        self.alphabet = newAlphabet
        #Alphabet = [[0,0,0,0,0],[0,56,125,56,0],[80,96,0,80,96],[20,127,20,127,20],[18,42,127,42,36],[98,100,8,19,35],[54,73,85,34,5],[0,80,96,0,0], [0,28,34,65,0],[0,65,34,28,0],[20,8,62,8,20],[8,8,62,8,8],[0,5,6,0,0],[8,8,8,8,8],[0,3,3,0,0],[2,4,8,16,32],[62,69,73,81,62],[17,33,127,1,1],[33,67,69,73,49],[34,65,73,73,54],[12,20,36,127,4],[114,81,81,81,78],[62,73,73,73,38],[64,71,72,80,96],[54,73,73,73,54],[50,73,73,73,62],[0,54,54,0,0],[0,53,54,0,0],[8,20,34,65,0],[20,20,20,20,20],[0,65,34,20,8],[32,64,69,72,48],[62,73,87,85,62],[31, 36, 68, 36, 31],[127, 73, 73, 73, 54],[62, 65, 65, 65, 34],[127, 65, 65, 34, 28],[127, 73, 73, 65, 65],[127, 72, 72, 72, 64],[62, 65, 65, 69, 38],[127, 8, 8, 8, 127],[0, 65, 127, 65, 0],[2, 1, 1, 1, 126],[127, 8, 20, 34, 65],[127, 1, 1, 1, 1],[127, 32, 16, 32, 127],[127, 32, 16, 8, 127],[62, 65, 65, 65, 62],[127, 72, 72, 72, 48],[62, 65, 69, 66, 61],[127, 72, 76, 74, 49],[50, 73, 73, 73, 38],[64, 64, 127, 64, 64],[126, 1, 1, 1, 126],[124, 2, 1, 2, 124],[126, 1, 6, 1, 126],[99, 20, 8, 20, 99],[96, 16, 15, 16, 96],[67, 69, 73, 81, 97],[0,127,65,65,0],[32,16,8,4,2],[0,65,65,127,0],[16,32,64,32,16],[1,1,1,1,1],[0,64,32,16,0],[2,21,21,14,1],[64,126,9,17,14],[14,17,17,17,10],[14,17,74,127,1],[14,21,21,21,9],[1,9,63,72,32],[9,21,21,21,30],[127,8,8,8,7],[0,0,46,1,1],[2,1,1,1,94],[1,127,4,10,17],[0,65,127,1,0],[31,16,14,16,31],[31,8,16,16,15],[14,17,17,17,14],[127,20,20,20,8],[8,20,20,31,1],[31,8,16,16,8],[9,21,21,21,18],[16,16,126,17,18],[30,1,1,30,1],[28,2,1,2,28],[30,1,6,1,30],[17,10,4,10,17],[16,9,6,8,16],[17,19,21,25,17],[8,54,65,65,0],[0,0,127,0,0],[0,65,65,54,8],[32,64,32,16,32]]

    def writeRegisters(self):
        IO.output(self.rclk_Pin,0)
        for i in range(self.numOfRegisterPins-1,-1,-1):
            IO.output(self.srclk_Pin,0)
            val = self.registers[i]
            IO.output(self.ser_Pin,val)
            IO.output(self.srclk_Pin,1)
        IO.output(self.rclk_Pin,1)

    def clearRegisters(self):
        for i in range(0,self.numOfRegisterPins):
            self.registers[i] = 0
        self.writeRegisters()

    def allDots(self, OnOff):
        oldFlipDelay = self.flipDelay
        #self.flipDelay = .01
        if(OnOff):
            for column in range(self.displayColumns):
                for row in range(self.displayRows):
                    self.registers[self.onColumns[column]]=1
                    self.registers[self.onRows[row]]=1
                    self.oldDisplayState[column][row]=1
                self.writeRegisters()
                sleep(self.flipDelay)
                self.clearRegisters()
        else:
            for column in range(self.displayColumns):
                for row in range(self.displayRows):
                    self.registers[self.offColumns[column]]=1
                    self.registers[self.offRows[row]]=1
                    self.oldDisplayState[column][row]=0
                self.writeRegisters()
                sleep(self.flipDelay)
                self.clearRegisters()   
        self.flipDelay = oldFlipDelay       
    
    def simpleTest(self, rowDot, columnDot):

        self.registers[self.onColumns[columnDot]]=1
        self.registers[self.onRows[rowDot]]=1
        self.writeRegisters()
        sleep(.2)
        self.clearRegisters()

        self.registers[self.offColumns[columnDot]]=1
        self.registers[self.offRows[rowDot]]=1
        self.writeRegisters()
        sleep(.2)
        self.clearRegisters()       

    def updateDisplay(self, textMessage, column_offset=0, row_offset=0):
        alphabetIndex = []
        currentColumn = 0
        character_size = 5
        currentDisplayState = [[0 for s in range(self.displayRows)] for c in range(self.displayColumns/character_size*len(textMessage)+1)]

        for character in range(len(textMessage)):
            alphabetIndex.append(ord(textMessage[character])-32)
            if alphabetIndex <0: 
                alphabetIndex=0

            for row in range(self.displayRows):
                currentDisplayState[character*(self.displayColumns/character_size)+character_size][row] = 0
            for character_column in range(character_size):
                columnbins= self.alphabet[alphabetIndex[character]]
                x = bin(columnbins[character_column])
                z = [bool(int(y)) for y in x[2:]]
                for f in range(7-len(z)):
                    z=[0]+z         
                row=0
                for isOn in z:
                    currentDisplayState[character*(self.displayColumns/character_size)+character_column][row] = isOn
                    row=row+1
        self.updateDisplayPixels(currentDisplayState, column_offset, row_offset)

    def updateDisplayPixels(self, currentDisplayState, column_offset=0, row_offset=0):
        needsUpdate = 0

        for column in range(min(self.displayColumns,len(currentDisplayState))):
            for row in range(self.displayRows):
                if currentDisplayState[column+column_offset][row] and not self.oldDisplayState[column][row]:
                    needsUpdate = 1
                    self.registers[self.onColumns[column]]=1
                    self.registers[self.onRows[row]]=1
            if needsUpdate:
                self.writeRegisters()
                sleep(self.flipDelay)
                self.clearRegisters()
                needsUpdate = 0
            for row in range(self.displayRows):
                if not currentDisplayState[column+column_offset][row] and self.oldDisplayState[column][row]:
                    needsUpdate = 1
                    self.registers[self.offColumns[column]]=1
                    self.registers[self.offRows[row]]=1
                self.oldDisplayState[column][row] = currentDisplayState[column+column_offset][row]
            if needsUpdate:
                self.writeRegisters()
                sleep(self.flipDelay)
                self.clearRegisters()
                needsUpdate = 0


    def deInitialize(self):
        self.clearRegisters()
        IO.output(self.ser_Pin,0)
        IO.output(self.rclk_Pin,0)
        IO.output(self.srclk_Pin,0)
        IO.cleanup
        print("Goodbye!")
