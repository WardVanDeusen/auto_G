#!/usr/bin/env/python3
import sys
import os
import Xfeed
import Zfeed
import ipmFeedRates

def boxing():

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

# G-Code

  while myRoughStock > myPartDiameter:
    print(rapidCode,'X'"%0.4f"%myRoughStock,'Z'"%0.4f"%zZero,'F'"%0.1f"%rapidFeed)
    myRoughStock = myRoughStock - myCutDepth
    print(linearCode,'X',"%0.4f"%myRoughStock,'Z'"%0.4f"%myPartLength,'F'"%0.1f"%linearFeed)


