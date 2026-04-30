# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:47:02 2026

@author: rohit
"""

# summ of digits

a=int(input("entee the number :"))
sum=0
while(a!=0):
    rem=a%10
    sum=sum+rem
    a=a//10
print("sum of the digits is :",sum)