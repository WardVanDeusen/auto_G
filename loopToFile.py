from boxingMaths import _box as myBox
from ipmFeedRates import _ipm


class BoxingToFile(object):
    """create .nc file"""

    def __init__(self):
        # Name file and open

        # G-Code
        fileName = input('Name file: ')
        with open(fileName, 'w') as f:
            while myBox.myRoughStock > myBox.myPartDiameter:
                f.write(_ipm.rapidCode)
                f.write(' X'"%0.4f" % myBox.myRoughStock)
                f.write(' Z'"%0.4f" % myBox.zZero)
                f.write(' F'"%0.1f" % _ipm.rapidFeed)
                f.write('\n')

                myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

                f.write(_ipm.linearCode)
                f.write(' X'"%0.4f" % myBox.myRoughStock)
                f.write(' Z'"%0.4f" % myBox.myPartLength)
                f.write(' F'"%0.1f" % _ipm.linearFeed)
                f.write('\n')


_B2f = BoxingToFile()
