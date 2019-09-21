#! python3
import Xfeed
import Zfeed

myX = Xfeed.X()
myZ = Zfeed.Z()


class Box:
    def __init__(self):
        """boxing cuts for blanking part diameters"""

#       X-axis movement
        self.myCutDepth = myX.myCutDepth
        self.myRoughStock = myX.myRoughStock
        self.myPartDiameter = myX.myPartDiameter
        self.xCuts = (self.myCutDepth /
                      (self.myRoughStock - self.myPartDiameter))

#       Z-axis movement
        self.zZero = myZ.zZero
        self.myPartLength = myZ.myPartLength


Box()
