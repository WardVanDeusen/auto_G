#! python3
import sys
import os
import Xfeed
import Zfeed
import ipmFeedRates

# Feedrates
linearCode = ipmFeedRates.linearCode
rapidCode = ipmFeedRates.rapidCode
linearFeed = ipmFeedRates.linearFeed
rapidFeed = ipmFeedRates.rapidFeed

#X-axis movement
myCutDepth =  Xfeed.myCutDepth
myRoughStock = Xfeed.myRoughStock
myPartDiameter = Xfeed.myPartDiameter
xCuts = (myCutDepth/(myRoughStock-myPartDiameter))

#Z-axis movement
zZero = Zfeed.zZero
myPartLength = Zfeed.myPartLength


