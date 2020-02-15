# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:28:01 2020

@author: PALAK DHINGRA
"""

import os

def renameFiles():
    #(1) read fileNames from a folder
    path = r"<FILE PATH>"
    fileList = os.listdir(path)
    print(fileList)
    
    #(2) foreach fileName, renameFile
    for fileNameWithDigit in fileList:
        fileNameWithoutDigit = ''.join([i for i in fileNameWithDigit if not i.isdigit()]) 
        #fileNameWithoutDigit = fileNameWithDigit.translate(None,"0123456789")
        print(fileNameWithoutDigit)
        os.rename(os.path.join(path,fileNameWithDigit),os.path.join(path,fileNameWithoutDigit))
    

renameFiles()
