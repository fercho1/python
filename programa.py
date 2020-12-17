import RPi.GPIO as GPIO
import time
import os
from yeelight import Bulb

sensor = 10
contador = 0
foco = Bulb("192.168.1.130")

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setwarnings(False)
	
def loop():
	while True:
		channel = GPIO.wait_for_edge(sensor, GPIO.RISING, bouncetime = 1000)
		
		if channel is None:
			Pass
		else:
			global contador
			contador += 1
			os.system("clear")
			print "Movimiento detectado No. ", contador
			foco.turn_on()
			
			
		
		
def destroy():
	GPIO.cleanup()
	
if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
