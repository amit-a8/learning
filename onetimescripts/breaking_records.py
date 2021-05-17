#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    #print(scores)
    num_highest = 0
    num_lowest = 0
    lowest = scores[0]
    highest = scores[0]
    for i in range(1,len(scores)):
        if scores[i] < lowest:
            num_lowest = num_lowest + 1
            lowest = scores[i]
        elif scores[i] > highest:
            #print(scores[i], '   ', scores[i-1])
            num_highest = num_highest + 1
            highest = scores[i]
    return num_highest, num_lowest
