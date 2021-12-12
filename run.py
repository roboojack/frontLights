#!/user/bin/python

#just a little script to drive the front lights on a timer with the RaspPi Zero W

import RPi.GPIO as io
import time

io.setmode(io.BCM)
led1 = 27
io.setup(led1, io.OUT)

while 1:
    io.output(led1, True)
    time.sleep(1)
    io.output(led1, False)
    time.sleep(1)
