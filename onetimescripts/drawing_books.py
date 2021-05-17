#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = dict()
    for i in ar:
        if i in d.keys():
            d[i] = d[i] + 1
        else:
            d[i] = 1
    pair = 0
    for i in d.values():
        pair += int(i/2)
    return pair
