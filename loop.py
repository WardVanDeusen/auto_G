import boxingMaths
import ipmFeedRates

myBox = boxingMaths.Box()
var_rapidCode = ipmFeedRates._ipm.rapidCode
var_linearCode = ipmFeedRates._ipm.linearCode
var_linearFeed = ipmFeedRates._ipm.linearFeed
var_rapidFeed = ipmFeedRates._ipm.rapidFeed


class Boxing(object):
    """blanking part diameters"""

    def __init__(self):
        """G-Code"""
        while myBox.myRoughStock > myBox.myPartDiameter:
            print(var_rapidCode, 'X', myBox._x_in, 'Z'"%0.4f" %
                  myBox._z_in)
            print(var_linearCode, 'X'"%0.4f" % myBox.myRoughStock,
                  'Z'"%0.4f" % myBox.zZero, 'F'"%0.1f" % var_linearFeed)

            myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

            print('X', "%0.4f" % myBox.myRoughStock,
                  'Z'"%0.4f" % myBox.myPartLength,
                  'F'"%0.1f" % var_linearFeed)


_B = Boxing()
