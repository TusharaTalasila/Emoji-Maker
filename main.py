
 
 
import math
 
def baseMethod():
  turtle.penup()
  turtle.goto(0,faceShift)
  turtle.color(faceColor)
  turtle.begin_fill()
  turtle.circle(faceRad)
  turtle.end_fill()
 
def eyeMethod():
  eyes = str(input("What kind of eyes do you want your emoji to have (circle, slanted, crescent)? : "))
 
  if eyes == "circle":
    circle()
  
  elif eyes == "slanted":
    slantMethod()
  else:
    crescent()
 
def slantMethod():
  eyeColor = str(input("What color do u want your emoji eyes to be?:"))
  turtle.pencolor(eyeColor)
  turtle.width(15)
  turtle.penup()
  turtle.goto(20,(faceShift + 140))
  turtle.pendown()
  turtle.goto(80,(faceShift + 170))
  turtle.pencolor(eyeColor)
  turtle.penup()
  turtle.goto(-20,(faceShift + 140))
  turtle.pendown()
  turtle.width(15)
  turtle.goto(-80,(faceShift + 170))
  turtle.penup()
 
def circle():
  eyeColor = (input("What color do u want your emoji eyes to be?:"))
  turtle.penup()
  turtle.goto(45,(faceShift + 150))
  turtle.color(eyeColor)
  turtle.begin_fill()
  turtle.circle(20)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(-45,(faceShift + 150))
  turtle.color(eyeColor)
  turtle.begin_fill()
  turtle.circle(20)
  turtle.end_fill()
 
def crescent():
  eyeColor = str(input("What color do u want your emoji eyes to be?:"))
  turtle.penup()
  turtle.goto(53,(faceShift + 113))
  turtle.pendown()
  turtle.color(eyeColor)
  turtle.begin_fill()
  turtle.circle(30)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(53,(faceShift + 98))
  turtle.pendown()
  turtle.color(faceColor)
  turtle.begin_fill()
  turtle.circle(31)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(-53,(faceShift + 113))
  turtle.pendown()
  turtle.color(eyeColor)
  turtle.begin_fill()
  turtle.circle(30)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(-53,(faceShift + 98))
  turtle.pendown()
  turtle.color(faceColor)
  turtle.begin_fill()
  turtle.circle(31)
  turtle.end_fill()
 
def eyebrowMethod():
  brow = str(input("Do you want your emoji to have eyebrows?:"))
  if brow == "yes":
    browShape = str(input("What kind of eyebrows do you want your emoji to have (normal or angry)?: "))

    if browShape == "normal":
      normal()
    
    else:
      angry()

  else:
    print("Interesting!")
 
def normal():
  browColor = str(input("What color do you want the eyebrows to be?:  "))
  turtle.penup()
  #turtle.goto(-50,208)
  turtle.goto(-50,(faceShift + 220))
  turtle.setheading(175)
  turtle.pensize(5)     
  turtle.pendown()      
  turtle.fillcolor(browColor)
  turtle.pencolor(browColor)
  turtle.begin_fill()
  turtle.circle(60,60)
  turtle.end_fill()
  turtle.penup() 
  #turtle.goto(110,188)
  turtle.goto(110,(faceShift + 200))
  turtle.setheading(130)
  turtle.pensize(5)     
  turtle.pendown()      
  turtle.fillcolor(browColor)
  turtle.pencolor(browColor)
  turtle.begin_fill()
  turtle.circle(60,60)
  turtle.end_fill()
  turtle.penup()
 
def angry():
  browColor = str(input("What color do you want the eyebrows to be?:  "))
  turtle.goto(78,(faceShift+ 204))
  turtle.setheading(168)
  turtle.pensize(5)     
  turtle.pendown()      
  turtle.fillcolor(browColor)
  turtle.pencolor(browColor)
  turtle.begin_fill()
  turtle.circle(60,60)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(-12,(faceShift +185))
  turtle.setheading(132)
  turtle.pensize(5)     
  turtle.pendown()      
  turtle.fillcolor(browColor)
  turtle.pencolor(browColor)
  turtle.begin_fill()
  turtle.circle(60,60)
  turtle.end_fill()
  turtle.penup()
 
 
 
def mouthMethod():
  mouth = str(input("What kind of mouth do you want your emoji to have (happy, sad, meh)?:"))
  
  if mouth == "happy":
    happyMouth()
  
  elif mouth == "sad":
    sadMouth()
  
  else:
    mehMouth()
 
 
def happyMouth():
  mouthColor = str(input("What color do you want your emoji's mouth to be?: "))
  turtle.penup()
  turtle.goto(-2,(faceShift + 100))
  turtle.pendown()
  turtle.color(mouthColor)
  turtle.begin_fill()
  turtle.circle(40)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(-2,(faceShift + 125))
  turtle.pendown()
  turtle.color(faceColor)
  turtle.begin_fill()
  turtle.circle(41)
  turtle.end_fill()
  
def sadMouth():
  mouthColor = str(input("What color do you want your emoji's mouth to be?: "))
  turtle.penup()
  turtle.goto(0,(faceShift + 90))
  turtle.pendown()
  turtle.color(mouthColor)
  turtle.begin_fill()
  turtle.circle(40)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(0,(faceShift + 75))
  turtle.pendown()
  turtle.color(faceColor)
  turtle.begin_fill()
  turtle.circle(41)
  turtle.end_fill()
 
def mehMouth():
  mouthColor = str(input("What color do you want your emoji's mouth to be?: "))
  turtle.penup()
  turtle.pensize(5)
  turtle.pencolor(mouthColor)
  turtle.goto(-50,(faceShift + 80))
  turtle.pendown()
  turtle.goto(50,(faceShift + 80))

def tearMethod():
  tear = str(input("Do you want your emoji to have tears?"))
  if tear == "yes":
    tears()
  else:
    print("Okay!")
 
def tears():
  turtle.color("lightblue")
  turtle.penup()
  turtle.goto(67,(faceShift + 120))
  turtle.pendown()
  turtle.pensize(10)
  turtle.goto(67,(faceShift + 70))

  turtle.color("lightblue")
  turtle.penup()
  turtle.goto(-67,(faceShift + 120))
  turtle.pendown()
  turtle.pensize(10)
  turtle.goto(-67,(faceShift + 70))
  

def faceMethod():
  baseMethod()
  eyeMethod()
  eyebrowMethod()
  mouthMethod()
  tearMethod()
 
def maker():
  global faceColor
  global faceShift
  global faceRad
  global faceSize
  faceSize = float(input("What do you want your emoji's area to ((min = 55,000) (max = 70000)?: "))
  faceRad = ((faceSize/math.pi)**.5)
  faceShift = (-1*faceRad)
  faceColor = str(input("What color do you want your emoji to be?: "))
  turtle.goto(0,faceShift)
  turtle.mainloop()
  faceMethod()
 
import turtle
 
answer = str(input("Do you want to make an emoji?(yes or no): "))
i = 1
if answer == "yes":
  
  maker()
  rxn = str(input("Do you like your emoji?(yes or no):"))
  if rxn == "yes" :
    print("Yay! Come again soon!")
    i = int(input("Enter -99 to quit: "))
  
  while i > -99:
    turtle.clear()
    turtle.penup()
    turtle.goto(0,-1*faceShift)
    turtle.mainloop()
    maker()
    rxn = str(input("Do you like your emoji?(yes or no):"))
    if rxn == "yes" :
      print("Yay! Come again soon!")
      i = int(input("Enter -99 to quit: "))

 
if answer == "no":
  print("That sucks. Maybe next time!")


 
 
 

