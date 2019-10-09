import turtle

from new_project.project.package import boxingMaths


def __lines():
    myBox = boxingMaths.Box()

    wn = turtle.Screen()
    t = turtle
    _scale = 75
    myRoughStock = float((myBox.myRoughStock * _scale) * .5)
    myPartDiameter = float((myBox.myPartDiameter * _scale) * .5)
    myCutDepth = float((myBox.myCutDepth * _scale) * .5)
    myPartLength = float(myBox.myPartLength * _scale)
    _z_in = myBox._z_in * _scale
    _x_in = (myBox._x_in * _scale) * .5

    t.title('G-Code Simulator')
    t.shape('arrow')
    t.shapesize(.2, .2, 1)
    t.speed(1)

    t.penup()
    t.goto(_z_in, _x_in)
    t.pendown()

    while myRoughStock > myPartDiameter:

        t.pencolor('blue')
        t.goto(myBox.zZero, myRoughStock)
        t.goto(myPartLength, myRoughStock)
        t.pencolor('red')
        t.goto(_z_in, _x_in)
        myRoughStock = myRoughStock - myCutDepth
        _x_in = _x_in - myCutDepth

        if __name__ == '__main__':
            __lines()

    wn.exitonclick()
