import RPi.GPIO as GPIO
import pigpio
import time
import random
import multiprocessing
import signal
import sys

#This program interfaces GPIO pins (BCM pinout) with either a DB25 connector or Centronics 36 connector 
#for the purpose of parallel communications.  There are 3 one byte registers (Control, Status, Data).  These
#registers interface to the pin mapping below (See PIN_MAPPING)

#




#------------------------------------------------------------------------------------------------
#|                                         PIN_MAPPING                                          |
#+------------+-----------------+----------------+-----------+----------------+----------+------+
#| Pin (DB25) | Pin No (36 pin) |  Signal name   | Direction | Register - bit | Inverted | GPIO |
#+------------+-----------------+----------------+-----------+----------------+----------+------+
#| 1          | 1               | Strobe         | In/Out    | Control-0      | Yes      |   17 |
#| 2          | 2               | Data0          | Out       | Data-0         | No       |   27 |
#| 3          | 3               | Data1          | Out       | Data-1         | No       |   22 |
#| 4          | 4               | Data2          | Out       | Data-2         | No       |    5 |
#| 5          | 5               | Data3          | Out       | Data-3         | No       |    6 |
#| 6          | 6               | Data4          | Out       | Data-4         | No       |   13 |
#| 7          | 7               | Data5          | Out       | Data-5         | No       |   26 |
#| 8          | 8               | Data6          | Out       | Data-6         | No       |   23 |
#| 9          | 9               | Data7          | Out       | Data-7         | No       |   24 |
#| 10         | 10              | Ack            | In        | Status-6       | No       |    0 |
#| 11         | 11              | Busy           | In        | Status-7       | Yes      |    0 |
#| 12         | 12              | Paper-Out      | In        | Status-5       | No       |    0 |
#| 13         | 13              | Select         | In        | Status-4       | No       |    0 |
#| 14         | 14              | Linefeed       | In/Out    | Control-1      | Yes      |    0 |
#| 15         | 32              | Error          | In        | Status-3       | No       |    0 |
#| 16         | 31              | Reset          | In/Out    | Control-2      | No       |    0 |
#| 17         | 36              | Select-Printer | In/Out    | Control-3      | Yes      |    0 |
#| 18-25      | 19-30,33,17,16  | Ground         | -         | -              | -        | -    |
#+------------+-----------------+----------------+-----------+----------------+----------+------+

#Control Register
STROBE = 17
LINEFEED = -1
RESET = -1
PRINTER_SELECT = -1


#Status Register
ERROR = -1
SELECT_IN = -1
PAPER_OUT = -1
ACK = -1
BUSY = -1

#Data Register
DATA0 = 27
DATA1 = 22
DATA2 = 5
DATA3 = 6
DATA4 = 13
DATA5 = 26
DATA6 = 23
DATA7 = 24

GPIO.setmode(GPIO.BCM)

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
