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
        t.circle(50-i)
        t.position()
        print('shift to blue')
        t.pencolor("green")
        t.circle(25)
        print('shift to green')
        t.left(2)
        print(t.pos())
        t.circle(10)
        t.pencolor("red")
        t.circle(15,180)
        t.position()
        print('shift to red')
        t.pencolor("green")
        print("shift to green")
        t.pos()
        t.pencolor("red")
        t.position()
        print(t.pos())
        t.pos()
        print("shift to red")
        t.circle(10/i)
        t.pos()
        t.backward(num/5)
        t.pencolor("yellow")
        print("shift to yellow")
        tree(random.randint(1,100))
        tree(random.randint(1,num))
        print("End of random tree")
        t.pencolor("blue")
        print('shift to blue')
        t.circle(40/i)
        tree(random.randint(1,num/2))
        t.pencolor("green")
        print('shift to green')
        tree(random.randint(1,num/3))
        t.pos()
        tree(random.randint(1,num/2))
        t.pos()
        t.right(i)
        t.circle(10-i)
        t.forward(i)
        t.circle(10+i)
        t.left(i)
        t.circle(10-i)
        t.backward(i)
        t.circle(10+i)
        tree(random.randint(1,num))
        t.forward(num/5)
        t.right(2)
        t.pencolor("green")
        t.left(10)
        t.backward(10)
        t.right(15)
        t.forward(15)
        print('tree execution complete')

def cycle(i):
    if i<10:
        return 
    else:
        try:
            tree(random.randint(1,i))
            tree(random.randint(1,i*2))
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
         i-=1
        print('Exit loop0')
        t.tilt(45)
        while i>1:
         cycle(random.randint(1,i))
         print('Execution of loop i',i)
         i-=1
        print('Exit loop1')
        t.tilt(45)
        while (i-1)>1:
         cycle(random.randint(1,i-1))
         print('Execution of loop i-1',i-1)
         i-=1         
        print('Exit loop2')
        t.tilt(45)
        while (i-2)>1:
         cycle(random.randint(1,i-2))
         print('Execution of loop i-2',i-2)
         i-=1
        print('Exit loop3')
        t.tilt(45)
        while (i+1)>1:
         cycle(randome.randint(1,i+1))
         print('Execution of loop i+1',i+1)
         i-=1
        print('Exit final while loop')
        t.tilt(45)
        print('fractal execution complete')
val=input("Enter a num:")
num1=int(val)
tree(num1)
fractal(random.randint(1,num1))
turtle.done()
print('Simulation complete')
