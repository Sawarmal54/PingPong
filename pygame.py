import turtle
import winsound
wn = turtle.Screen()
wn.title("sawarmal")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0
#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350,0)

#pong
pong=turtle.Turtle()
pong.speed(0)
pong.shape("square")
pong.color("white")
pong.penup()
pong.goto(0,0)
pong.dx = 2
pong.dy = 2

#PEn 

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Courier", 24,"normal"))

#Function 
def paddle_a_up():
    y=paddle_a.ycor()
    y+=30
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=30
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=30
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=30
    paddle_b.sety(y)

#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



while True:
    wn.update()
    pong.setx(pong.xcor() +pong.dx)
    pong.sety(pong.ycor() +pong.dy)

    if pong.ycor() > 290:
        pong.sety(290)
        pong.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    elif pong.ycor() < -290:
        pong.sety(-290)
        pong.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if pong.xcor() > 390:
        pong.goto(0, 0)
        pong.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a,score_b), align="center", font=("Courier", 24,"normal"))

    elif pong.xcor() < -390:
        pong.goto(0 , 0)
        pong.dx *= -1
        score_b+=1
        pen.clear() 
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a,score_b), align="center", font=("Courier", 24,"normal"))


    if (pong.xcor()> 340 and pong.xcor() <350) and (pong.ycor() < paddle_b.ycor() + 40 and pong.ycor() >paddle_b.ycor() -40):
        pong.setx(340)
        pong.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (pong.xcor()< -340 and pong.xcor() >-350) and (pong.ycor() < paddle_a.ycor() + 40 and pong.ycor() >paddle_a.ycor() -40):
        pong.setx(-340)
        pong.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
