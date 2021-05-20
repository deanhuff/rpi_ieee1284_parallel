import RPi.GPIO as GPIO
import pigpio
import time
import random
import multiprocessing
import signal
import sys


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

p1 = multiprocessing.Process(target=flicker, args=[STROBE])
p1.start()
#p1.join()

def clean(arg1, arg2):
    p1.join()
    p1.terminate()
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGINT,clean)

data_pins = (DATA0, DATA1, DATA2, DATA3, DATA4, DATA5, DATA6, DATA7)

GPIO.setwarnings(False)
for pin in data_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

file = open("error.mp3", "rb")
mybyte = file.read(1)
counter=0
while mybyte:
    i=random.randrange(255)
#    i=byte
    # time.sleep(random.randint(100, 500) * 0.001)
    #GPIO.output(data_pins, (bytes(byte[0]&one[0]), bytes(byte[0]&two[0]), bytes(byte[0]&four[0]), bytes(byte[0]&eight[0]), bytes(byte[0]&sixteen[0]), bytes(byte[0]&thrirtytwo[0]),bytes(byte[0]&sixtyfour[0]), bytes(byte[0]&onetwentyeight[0])))
    #GPIO.output(data_pins, (i&1, i&2, i&4, i&8, i&16, i&32, i&64, i*128) )
    i=int.from_bytes(mybyte, 'big')
    GPIO.output(data_pins, (i&1, i&2, i&4, i&8, i&16, i&32, i&64, i&128) )
    if mybyte[0] < 33:
        print ("counter="+str(counter)+ " value=" + str(mybyte[0]) + " hex=" + hex(mybyte[0]))
    elif mybyte[0] > 126:
        print ("counter="+str(counter)+ " value=" + str(mybyte[0]) + " hex=" + hex(mybyte[0]))
    else:
        print ("counter="+str(counter)+ " value=" + str(mybyte[0]) + " hex=" + hex(mybyte[0]) + " chr=" + chr(mybyte[0]) )
    time.sleep(0.002)
    #time.sleep(random.randint(100, 500) * 0.001)
#    GPIO.output(data_pins, GPIO.LOW)
#    time.sleep(.01)
#    hexmbyte= [int(hex(mybyte).split('x')[0]
    mybyte=file.read(1)
    counter=counter+1
#    if (counter > 50):
#        break


p1.terminate()
sys.exit()

#p2 = multiprocessing.Process(target=flicker, args=[DATA0])
#p2.start()
#p3 = multiprocessing.Process(target=flicker, args=[DATA1])
#p3.start()
#p4 = multiprocessing.Process(target=flicker, args=[DATA2])
#p4.start()
#p5 = multiprocessing.Process(target=flicker, args=[DATA3])
#p5.start()
#p6 = multiprocessing.Process(target=flicker, args=[DATA4])
#p6.start()
#p7 = multiprocessing.Process(target=flicker, args=[DATA5])
#p7.start()
#p8 = multiprocessing.Process(target=flicker, args=[DATA6])
#p8.start()
#p9 = multiprocessing.Process(target=flicker, args=[DATA7])
#p9.start()
#
#p2.join()
#p3.join()
#p4.join()
#p5.join()
#p6.join()
#p7.join()
#p8.join()
#p9.join()
