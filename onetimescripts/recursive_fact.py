#!/bin/python

import sys
def cal_fact(num):
    if num == 1 or num ==0 :
        return 1
    else:
        return long(num * cal_fact(num-1))

a = int(raw_input())
print cal_fact(a)
