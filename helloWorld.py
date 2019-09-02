#!/usr/bin/python3
import sys

X = 0

fileName = input('Name file: ')
with open(fileName,'w') as f:
  while X < 100:
    X = X + 1
    f.write(str(X))
    f.write('\n')
