#! python3


class IpmFeedRates:
    """for holding all things feedrate"""

    def __init__(self):

        # Input
        self.linearCode = input('Enter linear feed code being used ')
        self.rapidCode = input('Enter rapid feed code being used ')
        self.linearFeed = float(input('Enter linear cutting feedrate '))
        self.rapidFeed = float(input('Enter rapid move feedrate '))
