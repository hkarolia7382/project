#SOS Flasher By Hari Karolia
import RPi.GPIO as GPIO,time
GPIO.setmode(GPIO.BOARD)
#Sets The Pin Numbering System For Ribbon Cable.
GPIO.setup(11,GPIO.OUT)
#'17' Is Pin Number
GPIO.output(11,True)
time.sleep(1)
GPIO.output(11,True)
GPIO.output(11,False)
GPIO.output(11,True)
GPIO.output(11,False)
GPIO.output(11,True)
GPIO.output(11,False)
GPIO.output(11,True)
time.sleep(1)
