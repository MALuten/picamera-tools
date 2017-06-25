#!/usr/bin/env python
from datetime import datetime, date, time
import RPi.GPIO as GPIO
import picamera
now = datetime.now()
print now
with picamera.PiCamera() as camera:
    
    camera.resolution = (2592, 1944)
    #camera.start_preview()
    #time.sleep(2)
    #camera.hflip = True
    #camera.vflip = True    
    camera.capture("/home/pi/camera/foto/" + str(now.strftime("%Y-%m-%d_%H%M%S")) + ".jpg")
    #camera.stop_preview()



