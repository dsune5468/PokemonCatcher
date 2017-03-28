from myProject import *
import turtle

#flexor

turtle.bgcolor("black")
turtle.colormode(255)
c = (155, 0, 10)

alice = turtle.Turtle()
alice.speed(0)

#trianglewithtubes
for times in range(500):
    alice.circle(100)
    alice.forward(times * 2)
    alice.left(60)
    alice.color(c)

h = turtle.Turtle()


#coolpattern
for i in(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    h.speed(0)
    h.right(45)

    h.color("white")
    h.circle(50)
    h.right(20)
    h.color("light gray")
    h.circle(100)
    h.circle(70)
    h.color("gray")
    h.circle(80)
    h.circle(90)
    h.left(10)
    h.color("light pink")
    h.right(5)

#flowercode

luke = turtle.Turtle()
luke.speed(0)

for times in range(10):
    flower(luke, 25)
    jump(luke, times * 4, times * 2)
    
    
    






    
    
    
    
    
    


    

    
    
    

turtle.done()
