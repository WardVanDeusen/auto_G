import boxingMaths
import ipmFeedRates


myBox = boxingMaths.Box(boxingMaths.xfeed, boxingMaths.zfeed)

rapidCode = ipmFeedRates.rapidCode
linearCode = ipmFeedRates.linearCode
linearFeed = ipmFeedRates.linearFeed
rapidFeed = ipmFeedRates.rapidFeed


def boxingToFile():

    # Name file and open

    # G-Code
    fileName = input('Name file: ')
    with open(fileName, 'w') as f:
        while myBox.myRoughStock > myBox.myPartDiameter:
            f.write(rapidCode)
            f.write(' X'"%0.4f" % myBox.myRoughStock)
            f.write(' Z'"%0.4f" % myBox.zZero)
            f.write(' F'"%0.1f" % rapidFeed)
            f.write('\n')

            myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

            f.write(linearCode)
            f.write(' X'"%0.4f" % myBox.myRoughStock)
            f.write(' Z'"%0.4f" % myBox.myPartLength)
            f.write(' F'"%0.1f" % linearFeed)
            f.write('\n')


boxingToFile()
