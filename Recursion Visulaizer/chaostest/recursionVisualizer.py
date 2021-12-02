import importlib
import inspect
import sys
import traceback
import turtle
import random
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
    if i<15:
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
                   t.forward(i*i)
                   t.left(60)
                   t.backward(i*i)
                   t.left(60)
                   t.forward(i*i)
                   if i%5 == 0:
                    for m in range(100):
                      t.pencolor("green")
                      t.forward(m)
                      t.right(90)
                      t.pencolor("red")
                      t.circle(20-m)
                      t.pencolor("orange")
                   t.forward(int(2*i/5))
        #tree(num1)
        print(t.pos())
        tree(2*i)
        print('tree execution complete')
        pass

def cycle(i:int,configuration: Configuration=None,secrets: Secrets=None)->None:
    if i<10:
        return 
    else:
        try:
            tree(i/2)
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
         tree(i)
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
