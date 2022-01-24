import turtle as t
t.shape('turtle')

def right():
    if player.xcor() < 200:
        player.fd(10)

def left():
    if player.xcor() > -200:
        player.bk(10)
        
t.bgcolor('silver')
t.setup(500, 700)


#플레이어
player = t.Turtle()
player.shape('square')
player.shapesize(1,5)
player.up()
player.speed(0)
player.goto(0, -270)

# 공
ball = t.Turtle()
ball.shape('circle')
ball.shapesize(1.3)
ball.up()
ball.speed(0)

t.listen()
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")

ball_xspeed = 5
ball_yspeed = 5


game_on = True
life = 3

#점수표시
t.up()
t.ht()
t.goto(0,300)
t.write(f'life : {life}', False, 'center',('',20))

while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)        

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() >340:
        ball_yspeed *= -1
        
    if ball.ycor() < -340:
        life -= 1
        t.clear()
        t.write(f'life : {life}', False, 'center', ('',20))
        ball.goto(0, 100)
        ball_yspeed *= -1
        ball_xspeed *= -1

    if life == 0:
        game_on = False
        t.goto(0,0)
        t.write("Game Over", False, "center",('',20))

    if player.distance(ball) < 50 and -260 < ball.ycor() < -240:
        ball_yspeed *= -1