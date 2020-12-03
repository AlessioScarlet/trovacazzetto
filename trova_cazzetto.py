# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:37:33 2020

@author: alessiosca
"""

from pyautogui import *
import pyautogui
import time

while 1:
    if pyautogui.locateOnScreen('cazzetto.png', confidence=0.8) != None:
        print("vedo il cazzetto")
        time.sleep(0.5)
    else:
        print("DOV'È IL CAZZETTO?!?!?")
        time.sleep(0.5)
