#!/bin/python3

import os
import sys


def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]
def countSubstrings(s, queries):
   
    outp = list()
    for each_query in queries:
        upper_val = each_query[1] + 1
        substr = s[each_query[0]: upper_val]
        all_substr = get_all_substrings(substr)
        all_substr = list(set(all_substr))
        outp.append(len(all_substr))
    return outp
    
