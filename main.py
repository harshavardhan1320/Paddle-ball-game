from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from score import ScoreBoard


s = Screen()
s.bgcolor("black")
s.setup(800, 600)
s.title("PONG")
s.tracer(0)

r_paddle = Paddle(0)
l_paddle = Paddle(1)

b = Ball()
sc = ScoreBoard()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(b.move_speed)
    s.update()
    b.move()


    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()

    if b.distance(r_paddle) < 50 and b.xcor() > 330 or b.distance(l_paddle) < 50 and b.xcor() < -330:
        b.bounce_x()


    if b.xcor() > 380:
        sc.increase_score_1()
        b.reset_position()

    if b.xcor() < -380:
        sc.increase_score_2()
        b.reset_position()



s.exitonclick()
