import boxingMaths
import ipmFeedRates


myBox = boxingMaths.Box()
myIpm = ipmFeedRates.IpmFeedRates()


class BoxingToFile:
    """for holding all things X coordinates"""

    def __init__(self):

            # Name file and open

            # G-Code
            fileName = input('Name file: ')
            with open(fileName, 'w') as f:
                while myBox.myRoughStock > myBox.myPartDiameter:
                    f.write(myIpm.rapidCode)
                    f.write(' X'"%0.4f" % myBox.myRoughStock)
                    f.write(' Z'"%0.4f" % myBox.zZero)
                    f.write(' F'"%0.1f" % myIpm.rapidFeed)
                    f.write('\n')

                    myBox.myRoughStock = myBox.myRoughStock - myBox.myCutDepth

                    f.write(myIpm.linearCode)
                    f.write(' X'"%0.4f" % myBox.myRoughStock)
                    f.write(' Z'"%0.4f" % myBox.myPartLength)
                    f.write(' F'"%0.1f" % myIpm.linearFeed)
                    f.write('\n')
