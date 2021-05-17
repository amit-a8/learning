#!/bin/python

import sys

def isValid(s):
    d= dict()
    for i in s:
        key = i
        d[key] = d.get(key, 0) + 1
    res = 'YES'
    prev_val = None
    already_fixed = False
    for key,val in d.iteritems():
        if prev_val == None:
            prev_val = val
        elif (prev_val - val) >=2 or (val - prev_val) >= 2:
            res = 'NO'
            break

        elif already_fixed == True and val != prev_val:
            res = 'NO'
        elif val == prev_val or val == prev_val + 1 or val == prev_val -1 :
            already_fixed = True
            res = 'YES'
        else:
            res = 'NO'
    return res

s = raw_input().strip()
result = isValid(s)
print(result)
