#!/bin/python3

import math
import os
import random
import re
import sys


def get_dict_from_list(list_item):
    item_dict = dict()
    for each_word in list_item:
        if each_word in item_dict:
            item_dict[each_word] = item_dict[each_word] + 1
        else:
            item_dict[each_word] =  1 
    return item_dict

def checkMagazine(magazine, note):
    ret = 'Yes'
    mag_dict = get_dict_from_list(magazine)
    note_dict = get_dict_from_list(note)
    for key, val in note_dict.items():
        if key not in mag_dict or val > mag_dict[key] :
            ret = 'No'
            break
    return ret
