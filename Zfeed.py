class _Z:
    """for holding all things Z coordinates"""

    def __init__(self):

        # constant
        self.zZero = float(0)

        # Input
        self._z_in = (float(input('Enter a Z-feed to cut engagement distance. ')))
        self.myPartLength = float(input('Enter the Z-axis major OD cut length. ')) * -1


_z = _Z()


if __name__ == '__main__':
        print('ZfeedOK')


else:
    _z_in = _z._z_in
    _z_part_length = _z.myPartLength
    _z_zero = _z.zZero
