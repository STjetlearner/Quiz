import pgzrun

WIDTH=700
HEIGHT=500

m=Rect(0, 0, 700, 50)

def draw():
    screen.draw.filled_rect(m, "dark blue")
    screen.draw.textbox("Welcome to Quiz Master!!!", m, color="black")

def move_marquee():
    m.x-=+2
    if m.right<0:
        m.left=700

def update():
    move_marquee()



pgzrun.go()