class _X(object):
    """for holding all things X coordinates"""

    def __init__(self):
        """Input"""
        self.myRoughStock = (float(input('Enter rough stock diameter ')))
        self.myPartDiameter = (float(input('Enter part diameter ')))
        self.myCutDepth = (float(input('Enter a depth of cut ')))
        self._x_in = (float(input('Enter a X-feed to cut engagement distance. ')) + self.myRoughStock)


if __name__ == '__main__':

        print('XfeedOK')

else:
        _x = _X()
        _x_roughstock = _x.myRoughStock
        x_part_diameter = _x.myPartDiameter
        _x_cut_depth = _x.myCutDepth
        _x_in = _x._x_in
