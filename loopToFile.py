#! python3
import sys
import os
import boxingBoxingMaths

def boxingToFile():

# Name file and open

# G-Code
  fileName = input('Name file: ')
  with open(fileName,'w') as f:
    while myRoughStock > myPartDiameter:
      f.write(rapidCode)
      f.write(' X'"%0.4f"%myRoughStock)
      f.write(' Z'"%0.4f"%zZero)
      f.write(' F'"%0.1f"%rapidFeed)
      f.write('\n')

      myRoughStock = myRoughStock - myCutDepth

      f.write(linearCode)
      f.write(' X'"%0.4f"%myRoughStock)
      f.write(' Z'"%0.4f"%myPartLength)
      f.write(' F'"%0.1f"%linearFeed)
      f.write('\n')
  return
boxingToFile()
