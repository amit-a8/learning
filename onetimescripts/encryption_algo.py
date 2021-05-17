#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    ##remove space
    s = s.replace(' ', '')
    n = len(s)
    sqrt_val = math.sqrt(n)
    num_rows = math.floor(sqrt_val)
    num_colm = math.ceil(sqrt_val)
    op_list = list()
    for i in range(num_rows):
        lower_lmt = i * num_colm
        upp_lmt = lower_lmt + num_colm
        op_list.append(s[lower_lmt: upp_lmt])
    op_str = str()
    length_op = len(op_list[0])
    print(op_list)
    for i in range(length_op):
        this_op_str = ''
        for each_str in op_list:
            if i < len(each_str):
                this_op_str += each_str[i]
        op_str += this_op_str + ' '
    return op_str
