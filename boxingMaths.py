from auto_G.input_output.cut_cycles import Xfeed as x
from auto_G.input_output.cut_cycles import Zfeed as z


class Box(object):
    def __init__(self):
        """boxing cuts for blanking part diameters"""

#   X-axis movement

        self.myCutDepth = x._x_cut_depth
        self.myRoughStock = x._x_roughstock
        self.myPartDiameter = (x.x_part_diameter /
                               (x._x_roughstock - x.x_part_diameter))
        self._x_in = x._x_in

#       Z-axis movement
        self.zZero = z._z_zero
        self.myPartLength = z._z_part_length
        self._z_in = z._z_in


if __name__ == '__main__':

        print('BMathOK')

else:
    _b = Box()
    _x_cut_depth = _b.myCutDepth
    _x_roughstock = _b.myRoughStock
    _x_part_diameter = _b.myPartDiameter
    _x_in = _b._x_in
    _z_zero = _b.zZero
    _z_part_length = _b.myPartLength
    _z_in = _b._z_in
