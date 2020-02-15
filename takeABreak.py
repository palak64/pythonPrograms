# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:01:01 2020

@author: PALAK DHINGRA
"""

 
import webbrowser
import time

totalBreak=3
breakCount=0
while breakCount<totalBreak:
    time.sleep(10);
    webbrowser.open('https://docs.python.org/2/library/webbrowser.html')
    totalBreak=totalBreak+1
