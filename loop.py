from auto_G.cutMaths import boxingMaths as b
from auto_G.input_output.cut_cycles.feeds_speeds import ipmFeedRates


class Boxing(object):

    var_rapidCode = ipmFeedRates._ipm.rapidCode
    var_linearCode = ipmFeedRates._ipm.linearCode
    var_linearFeed = ipmFeedRates._ipm.linearFeed
    var_rapidFeed = ipmFeedRates._ipm.rapidFeed
    myRoughStock = b._x_roughstock
    myPartDiameter = b._x_part_diameter
    myCutDepth = b._x_cut_depth
    myPartLength = b._z_part_length
    zZero = b._z_zero
    _z_in = b._z_in

    def __init__(self):
        """G-Code"""
        while self.myRoughStock > self.myPartDiameter:
                print(self.var_rapidCode, 'X', b._x_in, 'Z'"%0.4f" %
                      self._z_in)
                print(self.var_linearCode, 'X'"%0.4f" % self.myRoughStock,
                      'Z'"%0.4f" % self.zZero, 'F'"%0.1f" %
                      self.var_linearFeed)

                self.myRoughStock = self.myRoughStock - self.myCutDepth

                print('X', "%0.4f" % self.myRoughStock,
                      'Z'"%0.4f" % self.myPartLength,
                      'F'"%0.1f" % self.var_linearFeed)
