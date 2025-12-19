#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    arr=s.split(" ")
    new_arr=[]
    for i in arr:
        new_arr.append(i.capitalize())
    return " ".join(new_arr)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
