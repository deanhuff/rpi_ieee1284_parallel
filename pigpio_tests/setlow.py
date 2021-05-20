import RPi.GPIO as GPIO
import pigpio
import time
import random
import multiprocessing

GPIO.setmode(GPIO.BCM)
STROBE = 17
DATA0 = 27
DATA1 = 22
DATA2 = 5
DATA3 = 6
DATA4 = 13
DATA5 = 26
DATA6 = 23
DATA7 = 24

def flicker(pin):
    while(True):
        pi.write(pin, True)
        time.sleep(random.randint(100, 500) * 0.001)
        pi.write(pin, False)
        time.sleep(random.randint(100, 500) * 0.001)

pi = pigpio.pi()
pi.set_mode(STROBE, pigpio.OUTPUT)
pi.set_mode(DATA0, pigpio.OUTPUT)
pi.set_mode(DATA1, pigpio.OUTPUT)
pi.set_mode(DATA2, pigpio.OUTPUT)
pi.set_mode(DATA3, pigpio.OUTPUT)
pi.set_mode(DATA4, pigpio.OUTPUT)
pi.set_mode(DATA5, pigpio.OUTPUT)
pi.set_mode(DATA6, pigpio.OUTPUT)
pi.set_mode(DATA7, pigpio.OUTPUT)

data_pins = (DATA0, DATA1, DATA2, DATA3, DATA4, DATA5, DATA6, DATA7, STROBE)

GPIO.setwarnings(False)
for pin in data_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

