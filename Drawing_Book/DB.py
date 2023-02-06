#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
   return min(p // 2, (n - p + (n % 2 == 0)) // 2)    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()





"""
def pageCount(n, p):
    # Write your code here
    i=1
    if n%2!=0:
        j=n-1
    else:
        j=n    
    na=0
    if i>=p or j<=p:
        return na
    else:
        while i<=p or j>=p:
            i+=2
            j-=2
            na+=1
            if i>=p or j<=p:
                break
    return na    
    
    
"""