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
        return fractal(i)


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
         t.circle(i*i)
         t.seth(-i*i)
         t.pencolor("black")
         t.right(90)
         t.seth(i*i)
         t.circle(i*i)
         t.pencolor("green")
         #t.forward(2.5*i)
         t.left(45)
         t.circle(i*i)
         t.seth(i*i)
         t.onclick(t.goto)
         for i in range(num1):
             for j in range(i):
              t.pencolor("white")
              #t.forward(j/2)
              t.left(45)
              t.circle(i*i)
              t.right(45)
              if i>j:
                  for j in range(i):
                   t.pencolor("orange")
                   t.circle(j*i*num1)
                   t.left(45)
              else:
                  for j in range(i):
                   t.pencolor("green")
                   t.circle(j*j*j)
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
             t.circle(l*l)
             t.right(90)
             t.seth(i*i)
             t.pencolor("white")
             t.circle(l*l)
             t.left(45)
         t.onclick(t.goto)
         t.right(45)
         #t.forward(-2*i)
         t.circle(k*k)
         t.pencolor("yellow")
         t.seth(45)
         t.circle(k*k)
         t.onclick(t.goto)
         i-=1
        tree(5) 
        t.left(20)
        while i>0:
         t.pencolor("yellow")
         t.circle(20)
         i-=5
        tree(5)
        t.position()
        t.backward(15)
        while i>0:
         t.pencolor("black")
         t.circle(3*i)
         i-=1
        t.right(20)
        tree(5)
        while i>0:
         t.pencolor("yellow")
         t.circle(i*i)
         tree(i/2)
         i-=5
        tree(i)
        print(t.pos())
        t.pencolor("white")
        while (50-i)>0 and i>0:
         if (50-i)>0 and i>0:
                            tree(i)
                            t.circle(50-i)
                            i-=5
                            t.right(45)
                            i=i-5
                            t.forward(i)
                            i=i-5
                            t.left(45)
                            i=i-5
                            t.right(45)
         else:
             return
        print('Circle with radius',50-i)
        t.position()
        print('shift to blue')
        t.pencolor("green")
        print('shift to green')
        t.left(2)
        print(t.pos())
        t.pencolor("red")
        t.position()
        print('shift to red')
        t.tree(30)
        t.circle(30)
        t.pencolor("green")
        print("shift to green")
        t.pos()
        t.tree(50)
        t.circle(50)
        t.pencolor("red")
        t.position()
        print(t.pos())
        t.pos()
        print("shift to red")
        if (50-i)>0 and i>0:
                           t.circle(50-i)
                           t.right(45)
                           t.forward(i)
                           t.backward(i)
                           t.left(45)
                           i-=5
        else:
            return 
        print('Diminishing circle red',10-i)
        t.pos()
        t.backward(num/5)
        t.pencolor("yellow")
        print("shift to yellow")
        tree(num)
        print("End of random tree")
        t.pencolor("green")
        print('shift to green')
        t.right(90)
        t.pencolor("white")
        print('shift to white')
        while num>0:
         if num>0:
          tree(num)
          num-=1
         else:
             return
        t.pos()
        while num>0 & (num/2) % 2 == 0:
         tree(num/2) 
         t.pos()
         t.right(i)
        while (10-i)>1 and i>0:
         if (10-i)>0:
          t.circle(10-i)
          t.forward(i)
          i-=5
         else:
          return    
        print('Diminishing circle with radius',10-i)
        while (10+i)>0 and i>0:
         if (10+i)>0:
          t.circle(10+i)
          t.left(45)
          i-=5
         else:
          return   
        print('Diminishing circle with radius',10+i)
        while (10-i)>0 and i>0:
         t.circle(10-i)
         t.backward(i)
         i-=5
        print('Diminishing circle with radius',10+i)
        while (10+i)>0 and i>0:
         t.circle(10+i)
         i-=5
        print('Diminishing circle with radius',10+i)
        tree(random.randint(1,num))
        t.forward(num/5)
        while (2+i)>0 and (50-i)>0 and i>0:
         t.right(90)
         t.circle(50-i)
         i-=5
        t.pencolor("green")
        while (10+i)>0 and (50-i)>0 and i>0:
         t.left(90)
         t.circle(50-i)
         i-=5
        while (10-i)>0 and i>0:
         t.backward(10-i)
         i-=5
        while (15-i)>0 and (50-i)>0 and i>0:
         t.right(90)
         t.circle(50-i)
         i-=5
        while(15-i)>0 and (50-i)>0 and i>0:
         t.forward(90)
         t.circle(50-i)
         i-=5
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
        t.pos()
        t.tilt(30)
        t.right(50)
        while i>1:
         cycle(random.randint(1,i+1))
         i-=5
        print('Exit loop0')
        t.tilt(30)
        t.forward(50)
        while i>1:
         cycle(random.randint(1,i))
         print('Execution of loop i',i)
         i-=5
        print('Exit loop1')
        t.tilt(30)
        t.left(50)
        while (i-1)>1:
         cycle(random.randint(1,i-1))
         print('Execution of loop i-1',i-1)
         i-=5         
        print('Exit loop2')
        t.tilt(30)
        t.backward(50)
        while (i-2)>1:
         cycle(random.randint(1,i-2))
         print('Execution of loop i-2',i-2)
         i-=5
        print('Exit loop3')
        t.tilt(30)
        t.right(50)
        while (i+1)>1:
         cycle(random.randint(1,i+1))
         print('Execution of loop i+1',i+1)
         i-=5
        print('Exit final while loop')
        t.tilt(45)
        print('fractal execution complete')
        pass

val=input("Enter a num:")
num1=int(val)
def rec(num1:int,configuration: Configuration=None,secrets: Secrets=None)->Any:
 try:
  while num1>0:  
   #t.right(num1)
   #t.backward(num1)
   fractal(num1)
   #t.onclick(t.goto)
   #t.left(num1)
   #t.right(num1)
   num1-=1
 except:
  print('Fractal exception') 
  turtle.done()
  print('Simulation complete')
  pass
rec(num1)  
