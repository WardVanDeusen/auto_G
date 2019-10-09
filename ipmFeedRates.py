class IpmFeedRates(object):
    """all things feedrate"""

    def __init__(self):

        # Input
        self.linearCode = input('Enter linear feed code being used ')
        self.rapidCode = input('Enter rapid feed code being used ')
        self.linearFeed = float(input('Enter linear cutting feedrate '))
        self.rapidFeed = float(input('Enter rapid move feedrate '))


_ipm = IpmFeedRates()
var_rapid = _ipm.rapidCode
var_linear = _ipm.linearCode
var_linear_feed = _ipm.linearFeed
var_rapid_feed = _ipm.rapidFeed

# Test
# print(' ', var_rapid, '\n ', var_linear, '\n ', var_linear_feed, '\n ', var_rapid_feed)
