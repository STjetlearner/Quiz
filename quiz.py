import pgzrun

WIDTH=700
HEIGHT=500

m=Rect(0, 0, 700, 50)
a1=Rect(25, 375, 311.25, 100)
a2=Rect(25, 250, 311.25, 100)
a3=Rect(361.25, 250, 311.25, 100)
a4=Rect(361.25, 375, 311.25, 100)
t=Rect(525, 75, 150, 150)
q=Rect(25, 75, 475, 150)

def draw():
    screen.draw.filled_rect(m, "dark blue")
    screen.draw.textbox("Welcome to Quiz Master!!!", m, color="black")
    screen.draw.filled_rect(a1, "orange")
    screen.draw.textbox("a", a1, color="black")
    screen.draw.filled_rect(a2, "orange")
    screen.draw.textbox("b", a2, color="black")
    screen.draw.filled_rect(a3, "orange")
    screen.draw.textbox("c", a3, color="black")
    screen.draw.filled_rect(a4, "orange")
    screen.draw.textbox("d", a4, color="black")
    screen.draw.filled_rect(t, "dark green")
    screen.draw.textbox("time", t, color="dark blue")
    screen.draw.filled_rect(q, "dark green")
    screen.draw.textbox("question", q, color="dark blue")


def move_marquee():
    m.x-=+2
    if m.right<0:
        m.left=700

def update():
    move_marquee()

file_name="questions.txt"

allquestions=[]

fopen=open(file_name, "r")
for i in fopen:
    allquestions.append(i)

print(allquestions)

next_question==0

def read():
    for i in allquestions:
        print(allquestions[next_question])
        print()
        next_question=next_question+1

read()

pgzrun.go()