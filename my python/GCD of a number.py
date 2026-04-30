# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:27:25 2026

@author: rohit
"""

a=int(input("enter  a value:"))
b=int(input("enter b value :"))

while(b!=0):
    rem=a%b
    a=b
    b=rem
print("GCD :",a)
