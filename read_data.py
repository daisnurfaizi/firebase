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
z = [0,0,0] 
while True:
    nyala = firebase.get('/nyalakan', None)
    mati = firebase.get('/matikan', None)
    kipas = firebase.get('/kipas',None)
    #lampu = firebase.get('/lampu',None)
    a = len(kipas) 
    b = len(nyala) 
    c = len(mati)
    #d = len(lampu)
    if a == 1 and b == 1:
        print('kipas nyala')
        on(kipaspin)
        z.insert(0,1)
        print(z[0])
    elif a == 1 and b== 0:
        print('kipas mati')
        off(kipaspin)
        z.insert(0,0)
    elif z[0] == 1:
        print('kipas nyala')
        on(kipaspin)
    elif z[0] == 0:
        print('kipas mati')
        off(kipaspin)
    elif b==1:
        z.insert(1,1)
        print('lampu nyala')
        lampuon(lampupin)
    elif b ==0:
        z.insert(1,0)
        print('lampu mati')
        lampuoff(lampupin)
    elif z[1] == 1:
        print('lampu nyala')
        lampuon(lampupin)
    elif z[1] == 0:
        print('lampu mati')
        lampuoff(lampupin)
        
  #      on(kipaspin)
   # elif a == 1 and b== 1 and c == 1:
    #    print('kipas nyala')
     #   print(a,b,c)
   #     on(kipaspin)
    #    on(kipaspin)
    #elif b==1 and d==1:
    #    print(b)
    #    lampuon(lampupin)
    #elif c == 0 and d==1:
    #    print(c)
    #    lampuoff(lampupin)
    #elif a == 1 and c==0:
    #    print(c)
    #    off(kipaspin)
    