# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:40:23 2026

@author: rohit
"""

from datetime import datetime
import pytz
a=pytz.timezone("Asia/Kolkata")
b=datetime.now(a)
print(b)