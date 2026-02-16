import turtle

screen = turtle.Screen()
screen.title("Aditya in Colors")
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

t.goto(-150, 0)

name = "Aditya"
colors = ["red", "orange", "yellow", "green", "blue", "violet"]

step = 50  # fixed distance between letters

for i, ch in enumerate(name):
    t.color(colors[i % len(colors)])
    t.write(ch, align="center", font=("Courier", 40, "bold"))  # Courier ~ monospaced
    t.forward(step)  # always the same distance

turtle.done()
