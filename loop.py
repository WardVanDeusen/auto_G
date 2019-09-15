#! python3
import sys
import os
import boxingMaths

def boxing():

# Feedrates
  linearCode = boxingMaths.linearCode
  rapidCode = boxingMaths.rapidCode
  linearFeed = boxingMaths.linearFeed
  rapidFeed = boxingMaths.rapidFeed

#X-axis movement
  myCutDepth =  boxingMaths.myCutDepth
  myRoughStock = boxingMaths.myRoughStock
  myPartDiameter = boxingMaths.myPartDiameter
  xCuts = (myCutDepth/(myRoughStock-myPartDiameter))

#Z-axis movement
  zZero = boxingMaths.zZero
  myPartLength = boxingMaths.myPartLength

# G-Code

  while myRoughStock > myPartDiameter:
    print(rapidCode,'X'"%0.4f"%myRoughStock,'Z'"%0.4f"%zZero,'F'"%0.1f"%rapidFeed)
    myRoughStock = myRoughStock - myCutDepth
    print(linearCode,'X',"%0.4f"%myRoughStock,'Z'"%0.4f"%myPartLength,'F'"%0.1f"%linearFeed)

boxing()


