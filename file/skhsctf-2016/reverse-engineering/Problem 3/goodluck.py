#THE ULTIMATE ONE
import turtle
import time



wn = turtle.Screen()

#first shape
x = turtle.Turtle()
x.shape("circle")
x.shapesize(50)

#second shape
y = turtle.Turtle()
y.shape("circle")
y.shapesize(48)


#third shape
z = turtle.Turtle()
z.shape("circle")
z.shapesize(46)

#fourth shape
c = turtle.Turtle()
c.shape("circle")
c.shapesize(44)

#fith shape
v = turtle.Turtle()
v.shape("circle")
v.shapesize(42)
looper = 1

#sixth shape
b = turtle.Turtle()
b.shape("circle")
b.shapesize(40)
looper = 1

#sevnth shape
n = turtle.Turtle()
n.shape("circle")
n.shapesize(38)
looper = 1

#eighth shape
m = turtle.Turtle()
m.shape("circle")
m.shapesize(36)
looper = 1

#ninth shape
a = turtle.Turtle()
a.shape("circle")
a.shapesize(34)
looper = 1

#pass shape
pp = turtle.Turtle()
flag="hsctf{circle}"
pp.shapesize(34)
looper = 1

#thenth shape
s = turtle.Turtle()
s.shape("circle")
s.shapesize(32)
looper = 1

#eleventh shape
d = turtle.Turtle()
d.shape("circle")
d.shapesize(30)
looper = 1

#twelth shape
f = turtle.Turtle()
f.shape("circle")
f.shapesize(28)
looper = 1

#thirteenth shape
g = turtle.Turtle()
g.shape("circle")
g.shapesize(26)
looper = 1

#forteenth shape
h = turtle.Turtle()
h.shape("circle")
h.shapesize(24)
looper = 1

#play cicle
play = turtle.Turtle()
play.shape("circle")
play.shapesize(4, 8, 4)

looper = 0


while looper < 7:
    looper = looper + 1
    x.color("red") or x.color("purple")
    y.color("purple")
    z.color("yellow")
    c.color("lightblue")
    v.color("pink")
    b.color("orange")
    n.color("blue")
    m.color("green")
    d.color("yellow")
    f.color("red")
    g.color("purple")
    h.color("lightblue")
    play.color("yellow")
    play.pencolor("red")
    play.write("LOADING...", font = 20, align="center")
    time.sleep(0.5)

x.ht()
y.ht()
z.ht()
c.ht()
v.ht()
b.ht()
n.ht()
m.ht()
d.ht()
f.ht()
g.ht()
h.ht()
play.ht()
play.clear()
turtle.reset()

henrydidthispart = 1

import random
import time

snake = turtle.Turtle()
coin = turtle.Turtle()
scoreboard = turtle.Turtle()
scoreboard.shape("square")
scoreboard.shapesize(2, 3, 1)
scoreboard.pu()
scoreboard.setpos(-300, 300)
scoreboard.pencolor("green")
coin.ht()
wn = turtle.Screen()
wn.bgcolor("brown")
snake.color("hotpink")
snake.shape("square")
coin.color("yellow")
coin.shape("circle")
coin.pu()

snake.shapesize(1, 3, 1)
snake.pu()
snake.speed(0)
coin.speed(0)

def run():

    #inital setup
    snake_h = 1
    snake_w = 3
    snake_d = 1
    score = 0
    while henrydidthispart == 1:
        snake.fd(5)
        if coin.distance(snake) < 15:
            coin.setx(random.randint(-200, 200))
            coin.sety(random.randint(-200, 200))
            #increase width
            snake_w = snake_w + 1
            snake.shapesize(snake_h, snake_w, snake_d)
            #and then the score
            score = score + 10
            scoreboard.clear()
            #turtle.write("messi fan", font=("Arial", 16, "normal"))
            scoreboard.write(score, font = 16, align="center")




def spawn():
    coin.st()
    coin.setx(random.randint(-200, 200))
    coin.sety(random.randint(-200, 200))

def w():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def a():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def s():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def d():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)


def l():
    snake.write("please do not click L again or i will have to kill you")


wn.ontimer(run, 1)
wn.ontimer(spawn, 1)
wn.onkey(w, "w")
wn.onkey(d, "d")
wn.onkey(s, "s")
wn.onkey(a, "a")
wn.onkey(l, "l")


wn.listen()
wn.mainloop()
