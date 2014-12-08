#SOS Flasher By Hari Karolia

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD)

#Sets The Pin Numbering System For Ribbon Cable.

GPIO.setup(11,GPIO.OUT)

#Function Definition
def dot():
	GPIO.output(11,true) #Turns LED On
	time.sleep(0.5) #Wait
	GPIO.output(11,false) #Turns LED Off
	time.sleep(0.5)
#Defining The Dot() Function
dot()

#Function Definition 2
def dash():
	GPIO.output(11,true) #Turns LED On
        time.sleep(2) #Wait
        GPIO.output(11,false) #Turns LED Off
        time.sleep(0.5)
dash()


def a():
	dot()
	dash()
	print("A")
a()

def b()
	dash()
	dot()
	dot()
	dot()
	print("B")
b()

def c()
	dash()
	dot()
	dash()
	dot()
	print("C")
c()

def d()
	dash()
	dot()
	dot()
	print("D")
d()

def e()
	dot()
	print("E")
e()

def f()
	dot()
	dot()
	dash()
	dot()
	print("F")
f()

def g()
	dash()
	dash()
	dot()
	print("G")
g()

def h()
	dot()
	dot()
	dot()
	dot()
	print("H")
h()

def i()
	dot()
	dot()
	print("I")
i()

def j()
	dot()
	dash()
	dash()
	dash()
	print("J")
j()

def k()
	dash()
	dot()
	dash()
	print("K")
k()

def l()
	dot()
	dash()
	dot()
	dot()
	print("L")
l()

def m()
	dash()
	dash()
	print("M")
m()

def n()
	dash()
	dot()
	print("N")
n()
#Starting The Program

