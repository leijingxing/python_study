import turtle

# 设置画笔
t = turtle.Turtle()
t.speed(10)

# 绘制脸部轮廓
t.penup()
t.goto(0, -150)
t.pendown()
t.color("black", "#0099ff")
t.begin_fill()
t.circle(150)
t.end_fill()

# 绘制脸部白色部分
t.penup()
t.goto(0, -120)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(120)
t.end_fill()

# 绘制眼睛
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(x, y + 10)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

draw_eye(-30, 80)
draw_eye(30, 80)

# 绘制鼻子
t.penup()
t.goto(0, 50)
t.pendown()
t.color("black", "#e60000")
t.begin_fill()
t.circle(15)
t.end_fill()

# 绘制嘴巴
t.penup()
t.goto(0, 50)
t.pendown()
t.setheading(-90)
t.forward(40)
t.penup()
t.goto(-80, 10)
t.pendown()
t.setheading(-30)
t.circle(100, 60)

# 绘制胡须
def draw_whisker(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(angle)
    t.forward(60)

draw_whisker(-40, 40, 160)
draw_whisker(-40, 30, 180)
draw_whisker(-40, 20, 200)
draw_whisker(40, 40, 20)
draw_whisker(40, 30, 0)
draw_whisker(40, 20, -20)

# 绘制铃铛
t.penup()
t.goto(0, -90)
t.pendown()
t.color("black", "#ffff00")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(-30, -85)
t.pendown()
t.color("black", "#e60000")
t.begin_fill()
t.circle(50, 60)
t.left(120)
t.circle(50, 60)
t.end_fill()

# 隐藏画笔
t.hideturtle()

# 完成
turtle.done()