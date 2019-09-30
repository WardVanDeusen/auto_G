from boxingMaths import _box as myBox
from ipmFeedRates import _ipm as myIpm
from clearScreen import clear

_clear = clear


class Boxing(object):
    """blanking part diameters"""

    def __init__(self):

        """G-Code"""
        while myBox.myRoughStock > myBox.myPartDiameter:
            print(myIpm.rapidCode, 'X', myBox._x_in, 'Z'"%0.4f" %
                  myBox._z_in)
            print(myIpm.linearCode, 'X'"%0.4f" % myBox.myRoughStock,
                  'Z'"%0.4f" % myBox.zZero, 'F'"%0.1f" % myIpm.linearFeed)

            myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

            print('X', "%0.4f" % myBox.myRoughStock,
                  'Z'"%0.4f" % myBox.myPartLength,
                  'F'"%0.1f" % myIpm.linearFeed)


_B = Boxing()
