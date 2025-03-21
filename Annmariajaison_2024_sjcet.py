from turtle import *

speed(0)
pensize(2)

goto(10, -1.5)  # Move to the center
pendown()


# Draw the new circle
color("dark slate blue")  # Color of the new circle
begin_fill()

circle(127)  # Size of the new circle

end_fill()

# Draw outer pattern of circles
goto(0, 0)
color("orange", "lime green")
begin_fill()

for i in range(40):
    
    circle(40)
    forward(20)
    left(9)

end_fill()

# Move the turtle to a new position for the star-like pattern
penup()
goto(2, 80)  # Center position
pendown()

# Draw star-like pattern with smaller circles
color("mediumvioletred", "goldenrod")
begin_fill()

for i in range(20):
    circle(20)  # Smaller size
    penup()
    forward(15)  # Adjust forward distance
    pendown()
    left(18)

end_fill()

done()
