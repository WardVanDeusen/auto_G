import boxingMaths
import ipmFeedRates

myBox = boxingMaths.Box()

rapidCode = ipmFeedRates.rapidCode
linearCode = ipmFeedRates.linearCode
linearFeed = ipmFeedRates.linearFeed
rapidFeed = ipmFeedRates.rapidFeed


def boxing():
    # G-Code
    while myBox.myRoughStock > myBox.myPartDiameter:
        print(rapidCode, 'X'"%0.4f" % myBox.myRoughStock,
              'Z'"%0.4f" % myBox.zZero, 'F'"%0.1f" % rapidFeed)
        myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

    print(linearCode, 'X', "%0.4f" % myBox.myRoughStock,
          'Z'"%0.4f" % myBox.myPartLength, 'F'"%0.1f" % linearFeed)


boxing()
