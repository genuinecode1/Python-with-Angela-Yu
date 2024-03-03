from turtle import Turtle, Screen
import random
#importing all classes of any module
# from turtle import *
#import module as alias
# import turtle as t
#installing module
#sometimes importing the module us not enough we have to install the module
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


def square():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


def dotted_path():
    for i in range(0,20):
        if i%5==0:
            timmy_the_turtle.left(90)
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


color = ["red","green","blue","orange","violet","purple","cyan","indigo","yellow"]
def print_shape():
    col = 0
    def turn_move(angle,distance):
        timmy_the_turtle.forward(distance)
        timmy_the_turtle.left(angle)
    for i in range(3,11):
        for j in range(0,i):
            timmy_the_turtle.color(color[col])
            turn_move(angle=360/i,distance=100)
        col += 1


def random_walk():
    l = True
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.speed("fastest")
    for i in range(0,300):
        walk = random.randint(30,40)
        random_color = random.randint(0,8)
        angle = random.randint(0,90)
        timmy_the_turtle.forward(walk)
        if l:
            timmy_the_turtle.left(angle)
            l = False
        else:
            timmy_the_turtle.right(angle)
            l= True
        timmy_the_turtle.color(color[random_color])


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        random_color = random.randint(0, 8)
        timmy_the_turtle.color(color[random_color])
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size_of_gap)


timmy_the_turtle.speed("fastest")
# square()
# dotted_path()
# print_shape()
# random_walk()
draw_spirograph(5)






# screen is used to show up the screen wg=hile running the program
screen = Screen()
screen.exitonclick()

