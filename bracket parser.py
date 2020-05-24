# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:21:34 2019

@author: Adi
"""

formula = input("Enter a formula: ")

stack = []
balanced = True

for character in formula:
    if character == "(":
        stack.append(character)
    elif character == ")":
        if len(stack) == 0:
            balanced = False
            break
        else:
            stack.pop(len(stack)-1)

if balanced and (len(stack) == 0):
    print("Formula is good")
else:
    print("Formula is wrong")
    
