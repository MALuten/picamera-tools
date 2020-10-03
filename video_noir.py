#!/usr/bin/env python
import picamera
import RPi.GPIO as GPIO
from datetime import datetime, date, time
now = datetime.now()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

try:
    GPIO.output(7, GPIO.HIGH)
    with picamera.PiCamera() as camera:
	camera.resolution = (1920, 1080)
	print "Recording!"
	camera.start_recording("/home/pi/camera/" + str(now.strftime("%Y-%m-%d_%H%M%S")) + ".h264")
	while (True):
		print "Recording!"

except KeyboardInterrupt:
	GPIO.output(7, GPIO.LOW)
	GPIO.cleanup()
	#camera.stop_recording()
	
	print "KeyboardInterrupt"