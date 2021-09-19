import turtle
import random
from turtle import *
t = turtle.Turtle()
num=random.randint(1,1000)
t.right(num)
t.speed(num)
t.left(num) 
def tree(i):
    if i<10:
        return
    else:
        t.right(15)
        turtle.heading()
        t.forward(15)
        t.left(20)
        t.position()
        t.backward(20)
        print(t.pos())
        t.pencolor("blue")
        while (50-i)<2:
         t.circle(50-i)
         tree(50-i)
         i=i-5
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
        t.pencolor("green")
        print("shift to green")
        t.pos()
        t.pencolor("red")
        tree(i*3)
        t.position()
        print(t.pos())
        t.pos()
        print("shift to red")
        while (50-i)>1:
         t.circle(random.randint(50-i))
         i-=10
        print('Diminishing circle red',10-i)
        t.pos()
        t.backward(num/5)
        t.pencolor("yellow")
        print("shift to yellow")
        tree(random.randint(1,100))
        tree(random.randint(1,num))
        print("End of random tree")
        t.pencolor("blue")
        print('shift to blue')
        tree(random.randint(1,num/2))
        t.pencolor("green")
        print('shift to green')
        while num>0:
         tree(num)
         num-=1
        t.pos()
        while num>0:
         tree(num/2)
         num-=1
        t.pos()
        t.right(i)
        while (10-i)>1:
         t.circle(10-i)
         t.forward(i)
         i-=2
        print('Diminishing circle with radius',10-i)
        while (10+i)>1:
         t.circle(10+i)
         t.left(i)
         i-=2
        print('Diminishing circle with radius',10+i)
        while (10-i)>1:
         t.circle(10-i)
         t.backward(i)
         i-=2
        print('Diminishing circle with radius',10+i)
        while (10+i)>1:
         t.circle(10+i)
         i-=2
        print('Diminishing circle with radius',10+i)
        tree(random.randint(1,num))
        t.forward(num/5)
        while (2+i)>0:
         t.right(2+i)
         t.circle(50)
         i-=1
        t.pencolor("green")
        while (10+i)>0:
         t.left(10+i)
         t.circle(50)
         i-=1
        while (10-i)>0:
         t.backward(10-i)
         i-=1
        while (15-i)>0:
         t.right(15-i)
         t.circle(50)
         i-=1
        while(15-i)>0:
         t.forward(15-i)
         t.circle(50)
         i-=1
        print('tree execution complete')

def cycle(i):
    if i<10:
        return 
    else:
        try:
            tree(random.randint(1,i))
        except:
            print('An exception occured')
        else:
            print('No Exception occured')   
        print('cycle loop complete')

def fractal(i):
    if i<10:
        return
    else:
        t.pos()
        t.tilt(45)
        while i>1:
         cycle(random.randint(1,i+1))
         i-=5
        print('Exit loop0')
        t.tilt(45)
        while i>1:
         cycle(random.randint(1,i))
         print('Execution of loop i',i)
         i-=5
        print('Exit loop1')
        t.tilt(45)
        while (i-1)>1:
         cycle(random.randint(1,i-1))
         print('Execution of loop i-1',i-1)
         i-=5         
        print('Exit loop2')
        t.tilt(45)
        while (i-2)>1:
         cycle(random.randint(1,i-2))
         print('Execution of loop i-2',i-2)
         i-=5
        print('Exit loop3')
        t.tilt(45)
        while (i+1)>1:
         cycle(random.randint(1,i+1))
         print('Execution of loop i+1',i+1)
         i-=5
        print('Exit final while loop')
        t.tilt(45)
        print('fractal execution complete')
val=input("Enter a num:")
num1=int(val)
try:
 fractal(random.randint(1,num1))
except:
 traceback.print_exec()
turtle.done()
print('Simulation complete')
