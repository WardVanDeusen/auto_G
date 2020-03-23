import Zfeed
import Xfeed

myX = Xfeed._X()
myZ = Zfeed._Z()


class Box(object):
    def __init__(self):
        """boxing cuts for blanking part diameters"""

#   X-axis movement

        self.myCutDepth = myX.myCutDepth
        self.myRoughStock = myX.myRoughStock
        self.myPartDiameter = myX.myPartDiameter
        self.xCuts = (self.myCutDepth /
                      (self.myRoughStock - self.myPartDiameter))
        self._x_in = myX._x_in

#       Z-axis movement
        self.zZero = myZ.zZero
        self.myPartLength = myZ.myPartLength
        self._z_in = myZ._z_in


if __name__ == '__main__':
    _box = Box()
