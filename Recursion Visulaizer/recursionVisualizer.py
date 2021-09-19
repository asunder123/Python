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
        t.setheading(0)
        t.left(20)
        t.setheading(90)
        t.position()
        t.setheading(180)
        t.backward(20)
        t.pencolor("blue")
        t.setheading(90)
        t.circle(5)
        t.position()
        print('shift to blue')
        t.setheading(0)
        tree(2*i/5)
        t.setheading(90)
        t.pencolor("green")
        t.circle(25)
        print('shift to green')
        t.left(2)
        t.setheading(180)
        t.circle(10)
        t.pencolor("red")
        t.circle(15)
        t.position()
        print('shift to red')
        t.pencolor("green")
        print("shift to green")
        tree(3*i/4)
        t.setheading(270)
        t.left(2)
        t.setheading(0)
        t.pencolor("red")
        t.position()
        t.tilt(10)
        print("shift to red")
        t.tilt(1)
        tree(i/2)
        t.circle(10)
        t.tilt(1)
        t.circle(10)
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
        t.tilt(5)
        print('shift to green')
        tree(random.randint(1,num/3))
        tree(random.randint(1,num/2))
        tree(random.randint(1,num))
        tree(random.randint(1,100))
        t.forward(num/5)
        t.right(2)
        tree(3*i/4)
        t.right(2)
        tree(2*i/5)
        t.pencolor("green")
        t.right(2)
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
            t.reset()
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
        turtle.position()
        print(t.position())
        t.tilt(45)
        cycle(random.randint(1,i+1))
        cycle(random.randint(1,i))
        cycle(random.randint(1,i-1))
        cycle(random.randint(1,i-2))
        t.title(45)
        t.circle(random.randint(1,i))
        print('fractal execution complete')
val=input("Enter a num:")
num1=int(val)
tree(num1)
fractal(random.randint(1,num1))
tree(num1)
turtle.done()
print('Simulation complete')
