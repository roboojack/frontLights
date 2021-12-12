#!/usr/bin/python

#just a little script to drive the front lights on a timer with the RaspPi Zero W

import RPi.GPIO as io
import time
import datetime

io.setmode(io.BCM)
led1 = 27
io.setup(led1, io.OUT)

while 1:
    # TODO: hook up a photo resistor in place of this
    # 1pm-5pm turn on
    if datetime.datetime.now().hour >= 12+5 or datetime.datetime.now().hour <= 12+1:
        io.output(led1, True)
    else:
        io.output(led1, False)

    time.sleep(1)
