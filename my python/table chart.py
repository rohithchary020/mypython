# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:46:25 2026

@author: rohit
"""
# table chart program
import time
print("\033[1;33m")
for i in range(1,11):
    time.sleep(1)
    for j in range(1,11):
        print("{:02d}".format(i*j),end=" ")
    print()