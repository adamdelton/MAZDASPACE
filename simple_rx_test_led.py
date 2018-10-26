#!/usr/bin/python3
#
# simple_rx_test.py
# 
# This is simple CAN receive python program. All messages received are printed out on screen.
# For use with PiCAN boards on the Raspberry Pi
# http://skpang.co.uk/catalog/pican2-canbus-board-for-raspberry-pi-2-p-1475.html
#
# Make sure Python-CAN is installed first http://skpang.co.uk/blog/archives/1220
#
# 01-02-16 SK Pang
#
#
#

import can
import time
import os
from dotstar import Adafruit_DotStar

numpixels = 77
brightness = 128

datapin = 23
clockpin = 24

print('\n\rCAN Rx test')
print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1)	

try:
	bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
	print('Cannot find PiCAN board.')
	exit()
	
print('Ready')

try:
	strip = Adafruit_DotStar(numpixels, datapin, clockpin, order='gbr'.encode('utf-8'))
	strip.begin()
	strip.setBrightness(brightness)

	while True:
		message = bus.recv()	# Wait until a message is received.

		print(message.data)
		print(range(message.dlc ))

		c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
		s=''
		for i in range(message.dlc ):
			s +=  '{0:x} '.format(message.data[i])
			print(message.data[i])
		print(' {}'.format(c+s))
		
		pointer = message.data[6]
		print(pointer)
		strip.clear()
		for i in range(5):
			strip.setPixelColor(pointer, 0xFF0000)
			pointer += 1
		strip.show()
	
except KeyboardInterrupt:
	#Catch keyboard interrupt
	os.system("sudo /sbin/ip link set can0 down")
	print('\n\rKeyboard interrtupt')	
	strip.clear()
	strip.show()
	strip.close()
