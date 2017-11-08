# list of Arduino USB IDs
# Each is specific to the **MODEL**
# Arduino MEGA:: idVendor=2a03, idProduct=0042
# Arduino Uno::  idVendor=2341, idProduct=0043
# Sparkfun Redboard:: idVendor=0403, idProduct=6015
# Ardunino Leonardo:: idProduct=0005

#import functions
import sys
import os
import subprocess
from subprocess import Popen
import serial

#create search IDs
Mega = "0042"
Uno = "0043"
Red = "6015"
Leo = "0005"

#look for ports attached
tmp = os.popen('python' ' -m' ' serial.tools.list_ports' ' -v').read()

#serach for typer of Arduino and captures its port
if Mega in tmp[:]:
    portUSB = tmp.split('\n', 1)
    print "Device is a Mega"
    print "It is attached to: " + portUSB[0]
    port = str(portUSB[0])
    port = port.strip()

if Uno in tmp[:]:
    portUSB = tmp.split('\n', 1)
    print "Device is an Uno"
    print "It is attached to: " + portUSB[0]
    port = str(portUSB[0])
    port = port.strip()

if Red in tmp[:]:
    portUSB = tmp.split('\n', 1)
    print "Device is a Redboard"
    print "It is attached to:"
    print "It is attached to: " + portUSB[0]
    port = port.strip()

if Leo in tmp[:]:
    portUSB = tmp.split('\n', 1)
    print "Device is a Leonardo"
    print "It is attached to:"
    print "It is attached to: " + portUSB[0]
    port = port.strip()

#attachs Arduino to ser
ser = serial.Serial(port, 115200, timeout = 1)
