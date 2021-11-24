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
         t.pencolor("red")
         #t.onclick(t.goto())
         t.circle(i*i*i)
         #t.seth(-i*i)
         t.pencolor("black")
         t.right(90)
         #t.seth(-i*i)
         t.circle(i*i*i)
         t.pencolor("green")
         #t.forward(2.5*i)
         t.left(45)
         t.circle(i*i*i)
         #t.seth(i*i)
         i+=1
         #t.onclick(t.goto)
         for i in range(num1):
             for j in range(i):
              t.pencolor("white")
              #t.forward(int(j/2*i))
              t.left(45)
              t.circle(i*j)
              t.right(45)
              if i>j:
                   t.pencolor("orange")
                   t.circle(i*j*num1-i*num1-i*j)
                   for j in range(num1):
                    t.pencolor("violet")
                    v=int(j/i)
                    while v<20:
                     t.forward(v)
                     t.left(90)
                     v+=1
                     j+=1
                   print('Shift to squaring')
                   t.pencolor("green")
                   t.forward(j)
                   t.right(90)
                   print("Position is ",t.pos())
                   if j%4==0:
                    for k in range(4):
                     t.pencolor("white")
                     t.forward(j*i*num1)
                     t.right(90)
              else:
                  for j in range(i):
                   t.pencolor("black")
                   t.circle(j*i*num1)
                   t.left(45)
              #if (i%j == 0):
               #for k in range(100):
                #t.forward((j/i)+1)
                #t.left(90)
              t.right(90)
              t.pencolor("green")
         for k in range(i):
          for j in range(k):
            for l in range(j):
             t.pencolor("black")
             t.circle(j*k*l)
             t.right(90)
             t.seth(i*i)
             t.pencolor("white")
             for m in range(l):
                 for n in range(m):
                  t.circle(m*n**l)
                  t.pencolor("red")
                  #t.forward(random.int(1,n/m))
                  t.left(90)
         t.onclick(t.goto)
         t.right(45)
         #t.forward(-2*i)
         t.circle(k*k*k)
         t.pencolor("yellow")
         #t.seth(-45*k*k)
         for m in range(l):
          for n in range(m):
            t.circle(l*l*l)
            t.right(45)
            tree(m)
        print(t.pos())
        print('tree execution complete')
        pass

def cycle(i:int,configuration: Configuration=None,secrets: Secrets=None)->None:
    if i<10:
        return 
    else:
        try:
            tree(i)
        except:
            print('An exception occured')
        else:
            print('No Exception occured')   
        print('cycle loop complete')
        pass

def fractal(i:int,configuration: Configuration=None,secrets: Secrets=None)->None:
    if i<10:
        return
    else:
        while i<num1:
         t.pencolor("white")   
         cycle(i)
         for j in range(num1):
          t.pencolor("green")
          t.forward(j)
          t.right(90)
         t.forward(int(i/num1))
         t.right(90)
         cycle(i+1)
         i+=1
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
