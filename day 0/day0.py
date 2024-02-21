from turtle import *


#we want to paint a hause

#step 1: draw a square 
  
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of squure 

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)      #height of the door 
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,  200)
pendown()

color("black")
right(150)
forward(200)


exitonclick()
