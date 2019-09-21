import boxingMaths
import ipmFeedRates

myBox = boxingMaths.Box()
myIpm = ipmFeedRates.IpmFeedRates()


class Boxing:
    """for holding all things X coordinates"""

    def __init__(self):

        # G-Code
        while myBox.myRoughStock > myBox.myPartDiameter:
            print(myIpm.rapidCode, 'X'"%0.4f" % myBox.myRoughStock,
                  'Z'"%0.4f" % myBox.zZero, 'F'"%0.1f" % myIpm.rapidFeed)
            myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

        print(myIpm.linearCode, 'X', "%0.4f" % myBox.myRoughStock,
              'Z'"%0.4f" % myBox.myPartLength,
              'F'"%0.1f" % myIpm.linearFeed)
