#!/usr/bin/env python
from datetime import datetime, date, time
import RPi.GPIO as GPIO
from time import sleep
import picamera

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

now = datetime.now()
print now.strftime("%Y-%m-%d_%H%M%S")

GPIO.output(7, GPIO.HIGH)
with picamera.PiCamera() as camera:

        camera.resolution = (2592, 1944)
        camera.shutter_speed = 45000
        #camera.hflip = True
        #camera.vflip = True
        sleep(1)
        camera.capture("/home/pi/camera/fotoir/" + str(now.strftime("%Y-%m-%d_%H%M%S")) + ".jpg")

GPIO.output(7, GPIO.LOW)
GPIO.cleanup()
