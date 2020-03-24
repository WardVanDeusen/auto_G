import boxingMaths
import ipmFeedRates

myBox = boxingMaths.Box()
var_rapidCode = ipmFeedRates._ipm.rapidCode
var_linearCode = ipmFeedRates._ipm.linearCode
var_linearFeed = ipmFeedRates._ipm.linearFeed
var_rapidFeed = ipmFeedRates._ipm.rapidFeed


class BoxingToFile(object):
    """create .nc file"""

    def __init__(self):
        # Name file and open

        # G-Code
        fileName = input('Name file: ')
        with open(fileName, 'w') as f:
            while myBox.myRoughStock > myBox.myPartDiameter:
                f.write(var_rapidCode)
                f.write(' X'"%0.4f" % myBox._x_in)
                f.write(' Z'"%0.4f" % myBox._z_in)
                f.write(' F'"%0.1f" % var_rapidFeed)
                f.write('\n')
                f.write(var_linearCode)
                f.write(' X'"%0.4f" % myBox.myRoughStock)
                f.write(' Z'"%0.4f" % myBox.zZero)
                f.write(' F'"%0.1f" % var_linearFeed)
                f.write('\n')

                myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

                f.write('X'"%0.4f" % myBox.myRoughStock)
                f.write(' Z'"%0.4f" % myBox.myPartLength)
                f.write(' F'"%0.1f" % var_linearFeed)
                f.write('\n')
