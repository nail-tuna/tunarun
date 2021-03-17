import turtle as t
import random

score = 0
playing = False

#못참치
tuna = ['fish_east.gif','fish_north.gif','fish_west.gif','fish_south.gif']
for i in tuna:
    t.register_shape(i)


te = t.Turtle()
te.shape("arrow")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)


def turn_right():
    t.shape(tuna[0])
    t.setheading(0)


def turn_up():
    t.shape(tuna[1])
    t.setheading(90)


def turn_left():
    t.shape(tuna[2])
    t.setheading(180)


def turn_down():
    t.shape(tuna[3])
    t.setheading(270)


def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()


def play():
    global score
    global playing
    t.fd(10)
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5

    if speed > 15:
        speed = 15
    te.forward(speed)

    if t.distance(te) < 12:
        text = "score:" + str(score)
        message("game over", text)
        playing = False
        score = 0

    if t.distance(ts) < 12:
        score = score + 1
        t.write(score)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)

    if playing:
        t.ontimer(play, 100)


def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()


t.title("turtle run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape(tuna[0])

t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("turtle run", "[Space]")

wm = t.Screen()
wm.mainloop()


#if __name__ == '__main__':