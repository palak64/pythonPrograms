# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 01:49:10 2020
http://www.wdylike.appspot.com/?q=shot
Google's site to check curse words
@author: PALAK DHINGRA
"""
import urllib
import re

def readText():
    file = open(r"C:\Users\PALAK DHINGRA\.spyder-py3\CodingPython\UdacityPythonCode\movie_quotes.txt")
    fileContent = file.read()
    #print(fileContent)
    checkProfanity(fileContent)
    file.close()
    
def checkProfanity(text):
    print("http://www.wdylike.appspot.com/?q="+text)
    #removing tabs newline characters 
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+re.sub(r"\W","",text))
    print(connection.read())
    connection.close()
    
readText()
