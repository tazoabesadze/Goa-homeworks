#1 დვ იქნება ასეთი ! turtleში შექმენით სახლი ოღონდ რამე მარტივი არააა დაამატებთ გვერდძე კლდესავით რამეს ასევე დაამატებთ მზე 
#  და რაც გაგიხარდეთ თქვენ სურვილზეა ორონდ დამანახეთ რო ბევრი იშრიმეთ💚 წარმატებები ყველას

from turtle import*

speed(13)
width(3)

def squear():
    penup()
    goto(-100, -100)
    pendown()
    for i in range(4):
        forward(300)
        left(90)

def coordinates(x, y):
    penup()
    goto(x, y)
    pendown()

def panjris_kvadrati():
    for i in range(4):
        forward(70)
        left(90)


# კვადრატის დახატვა --->

begin_fill()
color("yellow")
squear()
end_fill()

# დამთავრდა კვადრატის დახატვა


# სახურავის დახატვა --->

coordinates(200, 200)
color("blue")
begin_fill()
left(140)
forward(200)
left(81)
forward(198)
end_fill()

# მორჩა სახურავის დახატვა


# კარების დახატვა --->

coordinates(10, -100)
color("red")
begin_fill()
right(131)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()

# მორჩა კარების დახატვა 


# ფანჯრების დახატვა --->

coordinates(-70, 150)
begin_fill()
color("white")
panjris_kvadrati()

coordinates(95, 150)
panjris_kvadrati()
end_fill()

# მორჩა ფანჯრების დახატვა

# გარაჟის დახატვა --->

coordinates(-100, 60)
color("blue")
begin_fill()
right(90)
forward(200)
left(90)
forward(160)
left(90)
forward(200)
end_fill()

# მორჩა გარაჟის დახატვა


# გარაჟის სახურავის დახატვა --->

coordinates(-100, 60)
color("purple")
begin_fill()
left(150)
forward(130)
left(66)
forward(110)
end_fill()

# მორჩა გარაჟის სახურავის დახატვა

# გარაჟის კარების დახატვა -->

coordinates(-250, -100)
color("red")
begin_fill()
right(126)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()

# მოვრჩი გარაჟის კარების დახატვა

# კლდის დახატვა --->

coordinates(-770, 350)
color("grey")
left(30)
forward(150)
left(70)
forward(100)
right(40)
forward(80)
forward(50)
right(80)
forward(400)
left(110)
forward(400)

coordinates(-70, -200)
forward(850)

coordinates(-250, -100)
right(74)
forward(110)

left(20)
forward(400)

coordinates(-150, -100)
forward(130)
left(10)
forward(400)

coordinates(650, 280)
color("yellow")
begin_fill()
circle(60)
end_fill()


exitonclick()