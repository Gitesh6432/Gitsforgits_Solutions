#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p=n=z=0
    num=len(arr)
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1        
    print(f"{p/num:.6f}\n{n/num:.6f}\n{z/num:.6f}")
            
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    def staircase(n):
    a = 1
    for i in range(1,n+1):
        print(" "*(n-a)+"#"*a)
        a+=1
    """        
    
    """
    def staircase(n):
    for i in range(1, n+1):
        l = i*'#'
        print(l.rjust(n))
    """        
    
    
    
