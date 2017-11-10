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

def find_port():
    #create search IDs
    Mega = "0042"
    Uno = "0043"
    Red = "6015"
    Leo = "0005"
    FTDI = "6014"
    FTDI_C = "6001"


    #look for ports attached
    tmp = os.popen('python' ' -m' ' serial.tools.list_ports' ' -v').read()
    print "Port Search complete"
    print tmp
    #serach for typer of Arduino and captures its port
    if Mega in tmp[:]:
        portUSB = tmp.split('\n', 1)
        print "Device is a Mega"
        print "It is attached to: " + portUSB[0]
        port = str(portUSB[0])
        port = port.strip()
        return port

    elif Uno in tmp[:]:
        portUSB = tmp.split('\n', 1)
        print "Device is an Uno"
        print "It is attached to: " + portUSB[0]
        port = str(portUSB[0])
        port = port.strip()
        return port

    elif Red in tmp[:]:
        portUSB = tmp.split('\n', 1)
        print "Device is a Redboard"
        print "It is attached to: " + portUSB[0]
        port = str(portUSB[0])
        port = port.strip()
        return port

    elif Leo in tmp[:]:
        portUSB = tmp.split('\n', 1)
        print "Device is a Leonardo"
        print "It is attached to: " + portUSB[0]
        port = str(portUSB[0])
        port = port.strip()
        return port
    elif FTDI in tmp[:]:
        portUSB = tmp.split('\n', 4)
        print "Device is a using a FTDI cable"
        print "It is attached to: " + portUSB[3]
        port = str(portUSB[3])
        port = port.strip()
        return port
    elif FTDI_C in tmp[:]:
        portUSB = tmp.split('\n', 4)
        print "Device is a using a USB FTDI Convertor"
        print "It is attached to: " + portUSB[3]
        port = str(portUSB[3])
        port = port.strip()
        return port
    elif Mega and Uno and Red and Leo and FTDI not in tmp[:]:
        print "no active port"
        port = "none"
        return port

#assigns port from function
port = str(find_port())
#attachs Arduino to ser
ser = serial.Serial(port, 115200, timeout = 1)
