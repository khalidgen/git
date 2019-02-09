import turtle
nbrSides = 10
for weirdname in range(nbrSides):
     turtle.forward(100)
     turtle.right(360/nbrSides)
     for moresteps in range(nbrSides) :      
          turtle.forward(50)
          turtle.right(360/nbrSides)

    
# turtle.mainloop()
# for colour in ['red','green','blue','black'] :
#     turtle.color(colour)
#     turtle.forward(100)
#     turtle.left(90)
# turtle.mainloop()    