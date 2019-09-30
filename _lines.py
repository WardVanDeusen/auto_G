import turtle
from boxingMaths import _box as myBox

wn = turtle.Screen()
t = turtle
_scale = 150
myRoughStock = float((myBox.myRoughStock * _scale) * .5)
myPartDiameter = float((myBox.myPartDiameter * _scale) * .5)
myCutDepth = float((myBox.myCutDepth * _scale) * .5)
myPartLength = float(myBox.myPartLength * _scale)
_x_in = myBox._x_in * _scale
_z_in = myBox._z_in * _scale

t.shape('arrow')
t.shapesize(.2, .2, 1)
t.speed(1)

t.penup()
t.goto(myPartLength + _z_in, myRoughStock + myBox._x_in)
t.pendown()

while myRoughStock > myPartDiameter:

    t.pencolor('blue')
    t.goto(myPartLength, myRoughStock)
    t.goto(0, myRoughStock)
    t.pencolor('red')
    t.goto(myPartLength + _z_in, myRoughStock + _x_in)
    myRoughStock = myRoughStock - myCutDepth
    print(myBox._x_in)

wn.exitonclick()
