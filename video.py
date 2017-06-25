#!/usr/bin/env python
import picamera
import RPi.GPIO as GPIO
from datetime import datetime, date, time
now = datetime.now()

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (1920, 1080)
        print "Aan het opnemen!"
        camera.start_recording("/home/pi/camera/video/" + str(now.strftime("%Y-%m-%d_%H%M%S")) + ".h264")
        while (True):
                print "Aan het opnemen!"

except KeyboardInterrupt:
        #camera.stop_recording()
        print "KeyboardInterrupt"

