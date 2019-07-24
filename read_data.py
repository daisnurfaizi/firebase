import sys
import time
import RPi.GPIO as GPIO
from firebase import firebase
firebase = firebase.FirebaseApplication('https://home-ehrlfa.firebaseio.com', None)
kipaspin = 11
lampupin = 13
def on(kipaspin):
    GPIO.output(kipaspin,GPIO.HIGH) 
    return
def off(kipaspin):
    GPIO.output(kipaspin,GPIO.LOW)
    return
def lampuoff(lampupin):
    GPIO.output(lampupin,GPIO.LOW)
    return
def lampuon(lampupin):
    GPIO.output(lampupin,GPIO.HIGH)
    return
GPIO.setmode(GPIO.BOARD)
GPIO.setup(kipaspin,GPIO.OUT)
GPIO.setup(lampupin,GPIO.OUT)
GPIO.setwarnings(False)
while True:
    nyala = firebase.get('/nyalakan', None)
    mati = firebase.get('/matikan', None)
    kipas = firebase.get('/kipas',None)
    lampu = firebase.get('/lampu',None)
    a = len(kipas)
    b = len(nyala)
    c = len(mati)
    d = len(lampu)
    if a == 1 and b == 1:
        print('kipas nyala')
        on(kipaspin)
    elif b==1 and d==1:
        print(b)
        lampuon(lampupin)
    elif c == 0 and d==1:
        print(c)
        lampuoff(lampupin)
    elif a == 1 and c==0:
        print(c)
        off(kipaspin)
    else:
        print('kipas mati')
        off(kipas)
        lampuoff(lampupin)
