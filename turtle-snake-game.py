#وارد کردن کتابخانه ها
import turtle
import time
import random
#تاخیر در زمان حرکت
delay = 0.1

#امتیازات
score = 0
high_score = 0

#صفحه
wn = turtle.Screen()
wn.title("Snake Game")#تایتل صفحه
wn.bgcolor('blue')#رنگ زمینه
wn.setup(600,600)#اندازه صفحه
wn.tracer(0)#صبر کردن برای اینکه کد ها کامل کشیده شود

#سر مار
head = turtle.Turtle()#شی برای رسم مار
head.speed(0)
head.shape("square")#شکل گذاری قلم
head.color("yellow")#رنگ مار
head.penup()
head.goto(0,0)
head.direction = "stop"#جهت قلم

#غذای مار
food= turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []#لیست برای نگهداری اجزای مار

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 24, "normal"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#وصل کردن پنجره به کیبورد
wn.listen()#واکنش نشان دادن نسبت به ورودی کاربر از کیبورد
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#MainLoop
while True:
    wn.update()

    #چک کردن برخورد مار با کناره های پنجره
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #پنهان کردن اجزای مار
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #خالی کردن لیست
        segments.clear()

        #ریست کردن امتیازز
        score = 0

        #ریست کردن تاخیر در حرکت
        delay = 0.1

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    #چک کردن برای برخورد با غذا
    if head.distance(food) <20:
        # بردن غذا در یک جای تصادفی
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #اضافه کردن جز جدید بدن
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        #کوتاه کردن تاخیر
        delay -= 0.001
        #اضافه کردن امتیاز
        score += 1

        if score > high_score:# بررسی اینکه امتیاز از بالا ترین امتیاز بییشتر است یا نه
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

    # حرکت قطعات بدن به ترتیب معکوس
    for index in range(len(segments)-1,0,-1):  # شروع از آخرین قطعه تا اولین قطعه
        x = segments[index-1].xcor()  # مختصات x قطعه قبلی
        y = segments[index-1].ycor()  # مختصات y قطعه قبلی
        segments[index].goto(x,y)  # انتقال قطعه فعلی به مکان قطعه قبلی

    #بردن اجزای بدن از سر تا آخر
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #چک کردن برخورد با بدن
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #مخفی کردن اجزا
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #تغییر امتیاز      
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
wn.mainloop()   