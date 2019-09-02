#!/usr/bin/python3

import sys
import helloWorld


def toFile():
  with open (helloWorld.fileName, 'w') as f:
    f.write(str(helloWorld.out))
    f.close()

toFile()

