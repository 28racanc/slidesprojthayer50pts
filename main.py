import turtle
from fileinput import lineno
import random
screen = turtle.Screen()
screen.screensize( 500,  500)










screen.bgcolor('white')


t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t.hideturtle()
t2.hideturtle()
t3.hideturtle()


t2.penup()
t2.goto(0,-350)
t2.pendown()
t2.write('Press enter to continue', font=('arial', 30, 'normal'), align='center')
t2.penup()
t.speed(0)
t.penup()
t.goto(0,100)
t.pendown()
t.write('Turtle', font=('arial', 30, 'normal'), align='center')


t.speed(0)


t.penup()
t.goto(0,-100)
t.pendown()
t.write('Presentation', font=('arial', 30, 'normal'), align='center')






t.penup()
t.goto(0,200)
t.pendown()
screen.addshape('turtleback-2-5leg.gif')
t.shape('turtleback-2-5leg.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(0,-200)
t.pendown()
screen.addshape('turtle.gif')
t.shape('turtle.gif')
t.stamp()
t.shape('classic')


t.penup()
t.fillcolor('green')
t.begin_fill()
t.goto(200,200)
t.setheading(0)
t.pendown()
t.goto(230,200)
t.goto(230,230)
t.goto(200,230)
t.goto(200,200)
t.end_fill()
round = input("Press enter to continue: ")
t.clear()










t.penup()
screen.bgcolor('orange')
t.goto(0,130)
t.pendown()
t.write('Favorite food(s)', font=('arial', 30, 'normal'), align='center')
t.penup()
t.goto(-200,0)
t.pendown()
screen.addshape('steak.gif')
t.shape('steak.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(-200,-100)
t.pendown()
t.write('Steak', font=('arial', 30, 'normal'), align='center')


t.penup()
t.goto(0,0)
t.pendown()
screen.addshape('cookies.gif')
t.shape('cookies.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(0,-100)
t.pendown()
t.write('Cookies', font=('arial', 30, 'normal'), align='center')




t.penup()
t.goto(200,0)
t.pendown()
screen.addshape('Uncrustables.gif')
t.shape('Uncrustables.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(200,-100)
t.pendown()
t.write('Uncrustables', font=('arial', 30, 'normal'), align='center')
t.penup()

t.penup()
t.goto(-225,-225)
t.fillcolor('purple')
t.begin_fill()
t.circle(30)
t.end_fill()

round = input("Press enter to continue: ")
t.clear()




# Hobbies
screen.bgcolor('green')


t.penup()
t.goto(0,130)
t.pendown()
t.write('Hobbies', font=('arial', 30, 'normal'), align='center')
t.penup()
t.goto(-220,0)
t.pendown()
screen.addshape('dirtbike2.gif')
t.shape('dirtbike2.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(-220,-100)
t.pendown()
t.write('Motocross', font=('arial', 30, 'normal'), align='center')
t.penup()
t.penup()
t.goto(-50,0)
t.pendown()
screen.addshape('goldengloves.gif')
t.shape('goldengloves.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(-50,-100)
t.pendown()
t.write('Boxing', font=('arial', 30, 'normal'), align='center')
t.penup()
t.penup()
t.penup()
t.goto(150,0)
t.pendown()
screen.addshape('drums.gif')
t.shape('drums.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(160,-100)
t.pendown()
t.write('Playing drums', font=('arial', 30, 'normal'), align='center')
t.penup()
t.goto(0,-200)
t.pendown()
screen.addshape('german.gif')
t.shape('german.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(00,-300)
t.pendown()
t.write('Exploring foreign languages', font=('arial', 30, 'normal'), align='center')
t.penup()

t.goto(200,180)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.setheading(0)
t.forward(50)
t.setheading(135)
t.forward(50)
t.setheading(245)
t.forward(40)
t.end_fill()
# t.setheading(0)
# t.forward(50)
round = input("Press enter to continue: ")
t.clear()




# movie
screen.bgcolor('dodger blue')


t.penup()
t.goto(0,130)
t.pendown()
t.write('Favorite Movie', font=('arial', 30, 'normal'), align='center')
t.penup()


t.penup()
t.goto(250,0)
t.pendown()
screen.addshape('earthecho1.gif')
t.shape('earthecho1.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(0,0)
t.pendown()
t.write('Earth To Echo', font=('arial', 30, 'normal'), align='center')
t.penup()




t.penup()
t.goto(-250,0)
t.pendown()
screen.addshape('earthecho2.gif')
t.shape('earthecho2.gif')
t.stamp()
t.shape('classic')
t.penup()

t.penup()
t.fillcolor('white')
t.begin_fill()
t.goto(-200,200)
t.setheading(45)
t.forward(50)
t.setheading(0)
t.setheading(-45)
t.forward(50)
t.setheading(0)
t.setheading(-135)
t.forward(50)
t.setheading(135)
t.forward(50)
t.end_fill()

round = input("Press enter to continue: ")
t.clear()


screen.bgcolor('brown')




# Sport


t.penup()
t.goto(0,130)
t.pendown()
t.write('Favorite Sport', font=('arial', 30, 'normal'), align='center')
t.penup()


t.penup()
t.goto(250,0)
t.pendown()
screen.addshape('fb1.gif')
t.shape('fb1.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(0,0)
t.pendown()
t.write('American Football', font=('arial', 30, 'normal'), align='center')
t.penup()


t.penup()
t.goto(-250,0)
t.pendown()
screen.addshape('fb2.gif')
t.shape('fb2.gif')
t.stamp()
t.shape('classic')
t.penup()


t.penup()
t.goto(0,-200)
t.pendown()
screen.addshape('fb3.gif')
t.shape('fb3.gif')
t.stamp()
t.shape('classic')
t.penup()

t.goto(200,-200)
t.fillcolor('yellow')
t.begin_fill()
t.setheading(0)
t.pendown()
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.end_fill()
t2.clear()
# screen.addshape('turtle.gif')
# t.goto(0,0)
# t.shape('turtle.gif')
# t.stamp()
# t.shape('classic')


# t.write('Shock', font=('arial', 30, 'normal'), align='center')


# round = input("Press enter to continue: ")
turtle.done()
