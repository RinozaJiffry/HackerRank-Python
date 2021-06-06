#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if(n%2 == 0):
        if(2<=n and n>=5 or n>20):
            print("Not Weird")
        if(6<=n and n<=20 ):
            print("Weird")
    if(n%2 !=0):
        print("Weird")
