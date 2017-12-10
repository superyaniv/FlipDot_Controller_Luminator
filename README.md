# FlipDot Controller Project

A FlipDot board was a unique way, before the cheap and ubiquitous LED displays, to display signage with low power and high visability. The unique innovation combines electrical engineering princples of electromagnetism, polarity, multiplexing, and much more. Not to mention it's just fun to see the complex mechanical switching in realtime. As I became interested in learning more about electrical engineering and design, this project, created in 2011 and posted on my public git recently, inspired me to begin learning circuit design. 

## Getting Started

The PCB schemetic uses 10 shift registers to drive darlington array source and pull down ICs. The pin layout is explained in the cvs file. From there, the project uses the flipdot controller python class to post bytes to the board and pin layout. The layer of abstraction above that can be a variance of code, depending on what to pull and post to the board. Examples included here are a clock, bitcoin price feed, and twitter display.

### Prerequisites

Hardware necessary to complete the code from scratch include:

```
10 x 595 Shift Registers
5 x ULN2803 Darlington Arrays
5 x Source Drivers (x2981)
Note: A different layout could use MOSFET transistors instead of these ICs.

1 x microcontroller (RPI or ESP8266 for use with this python code or Arduino )
```

### View of the PCB

Top, Bottom, and overall Design View of the PCB:

<img align="left" src="https://github.com/superyaniv/FlipDot_Controller_Luminator/blob/master/PCB_Controller_Design/FlipDot_Controller_Pic_top.png?raw=true" width="250">
<img align="left"  src="https://github.com/superyaniv/FlipDot_Controller_Luminator/blob/master/PCB_Controller_Design/FlipDot_Controller_Pic_bottom.png?raw=true" width="250">
<img align="center"  src="https://github.com/superyaniv/FlipDot_Controller_Luminator/blob/master/PCB_Controller_Design/FlipDot_Controller_Pic_design.png?raw=true" width="250">

### Installing

Using the gerber files, you can have the board made at a host of pcb manufacturers. Alternatively you can design the board yourself with a breadboard.

Set up the layout of the board:

```
Using the gerber files, you can have the board made at a host of pcb manufacturers. 

Alternatively you can design the board yourself with a breadboard.
```

Wire your board:

```
Wire the board according to the schematic.

Connect the board to the flip-dot display and the microcontroller.
(use pins 18, 23, and 24 for the shift register data, clock, clear)
```


Connect to Power:

```
Connect the board to power, 9V for to drive the dots, and 5V to the registers.
```



End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Run tests to the shift registers first, to ensure the correct outputs from the registers.


Run tests to the source and pull drivers, to ensure the 9V supply is being triggered to the dots.

Use the attached LEDs to check power to the board.

If you are using APIs to get input for the display, check the output of those APIs by uncommenting the debug and print lines.

## Deployment

Add additional notes about how to deploy this on a live system

## Authors

Yaniv Joseph Alfasy (http://yanivalfasy.com)

Please contact me if you have any additional questions.

## License

No licensing decided yet.