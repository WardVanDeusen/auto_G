class _Z:
    """for holding all things Z coordinates"""

    def __init__(self):

        # constant
        self.zZero = float(0)

        # Input
        self._z_in = (float(input('Enter a Z-feed to cut engagement distance. ')))
        self.myPartLength = float(input('Enter the Z-axis major OD cut length. ')) * -1


if __name__ == '__main__':
    _z = _Z()
