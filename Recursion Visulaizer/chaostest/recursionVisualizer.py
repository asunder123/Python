import importlib
import inspect
import sys
import traceback
import turtle
import random
#import numpy as np
#import cv2
#import pyautogui
from typing import Any
from logzero import logger 
from chaoslib.types import Configuration, Secrets,Activity
from chaoslib.exceptions import ActivityFailed, InvalidActivity
from turtle import *



__all__ = ["cycle","tree","fractal","rec","line","steadystate"]
t = turtle.Turtle()
num=random.randint(900,1000)
t.right(num)
t.speed(1000*num)
t.left(num)
win = turtle.Screen()
win.bgcolor("blue")
win.setup(500,500)
win.title("setup")

def steadystate(i: int, configuration: Configuration = None, secrets: Secrets=None)->Any:
    if i<10:
        return
    else: 
        fractal(i)


def setup(i: int, configuration: Configuration = None, secrets: Secrets=None)->Any:
    if i<15:
       return 
    else:
        win = turtle.Screen()
        win.bgcolor("yellow")
        win.setup(height=1000,length=2000)
        #win.listen()
        #win.onkeypress(turtle.Turtle().set(20),"Up")
        #win.onkeypress(turtle.Turtle().set(20),"Down")
        win.title("setup")

def tree(i: int,configuration: Configuration = None,secrets: Secrets=None)->Any:
    if i<10:
        return
    else:
        setup(1)
        t.right(90)
        turtle.heading()
        t.forward(15)
        while i<num1:
         for i in range(num1):
              if i>10:
               t.pencolor("orange")
               for i in range(num1):
                   t.forward(i)
                   t.left(60)
                   t.backward(i)
                   t.left(60)
                   #t.forward(random.randint(int(i*i/2),i*i))
               for j in range(i):
                   t.pencolor("green")
                   t.forward(j)
                   t.right(90)
                   i+=i
               for i in range(num1):
                   win.listen()
                   win.onkeypress(turtle.Turtle().sety(i),"Up")
                   print("Turtle moved up by", t.pos())
                   win.onkeypress(turtle.Turtle().sety(-i),"Down")
                   print("Turtle moved down by",t.pos())
                   if i%2 == 0:
                    for m in range(i):
                      t.pencolor("green")
                      for j in range(m):
                       t.forward(j)
                       t.right(90)
                      t.pencolor("red")
                      t.circle(m-i)
                      t.pencolor("white")
                      for j in range(m):
                       t.forward(m-i)
                       t.right(60)
                       t.backward(m-i)
                       t.right(60)
                       t.forward(m-i)
                       print('Switch to random square')
                       for m in range(l):
                        t.pencolor("black")
                        t.forward(l*l)
                        t.right(90)
                        t.pencolor("yellow")
                        t.circle(l-m)
                      t.pencolor("orange")
                   #t.forward(int(2*i/5))
        tree(int(num1/5))
        print(t.pos())
        #tree(int(2*i/5))
        print('tree execution complete')
        pass

def cycle(i:int,configuration: Configuration=None,secrets: Secrets=None)->None:
    if i<10:
        return 
    else:
        try:
            tree(i)
        except:
            print('Cycle loop exception occured')
        else:
            print('No Exception occured')   
        pass

def fractal(i:int,configuration: Configuration=None,secrets: Secrets=None)->None:
    if i<10:
        return
    else:
        while i<num1:
         t.pencolor("white")   
         cycle(random.randint(int(3*i/4),int(1.5*i)))
        print('Exit final while loop')
        print('fractal execution complete')
        pass
val=input("Enter a num:")
num1=int(val)



def rec(i:int,configuration: Configuration=None,secrets: Secrets=None)->Any:
 try:
  while i<num1:  
   #t.right(num1)
   #t.backward(num1)
   fractal(i)
   i+=1
   #image = pyautogui.screenshot()
   #image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
   #cv2.imwrite("image1.png", image)
   #t.onclick(t.goto)
   #t.left(num1)
   #t.right(num1)
 except:
  print('Fractal exception') 
  turtle.done()
  print('Simulation complete')
  pass
print('Simulation begins')
rec(num1)
print('Take screenshot')

#turtle.getscreen().getcanvas().postscript(file='Image.eps', height=10000,width=10000)
