class _X(object):
    """for holding all things X coordinates"""

    def __init__(self):
        """Input"""
        self.myRoughStock = (float(input('Enter rough stock diameter ')))
        self.myPartDiameter = (float(input('Enter part diameter ')))
        self.myCutDepth = (float(input('Enter a depth of cut ')))
        self._x_in = (float(input('Enter a X-feed to cut engagement distance. ')) + self.myRoughStock)


if __name__ == '__main__':
    _x = _X()
