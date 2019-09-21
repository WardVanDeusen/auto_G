#! python3
import Xfeed as xfeed
import Zfeed as zfeed


class Box:
    def __init__(self):
        """comment"""

#       X-axis movement
        self.myCutDepth = xfeed.myCutDepth
        self.myRoughStock = xfeed.myRoughStock
        self.myPartDiameter = xfeed.myPartDiameter
        self.xCuts = (self.myCutDepth /
                      (self.myRoughStock - self.myPartDiameter))

#       Z-axis movement
        self.zZero = zfeed.zZero
        self.myPartLength = zfeed.myPartLength


Box()
