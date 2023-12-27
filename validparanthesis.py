# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:33:09 2023

@author: mpspb
"""

class Solution(object):
    def isValid(self, s):
       
        stack=[]
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i!= dict[a]:
                    return False
        return stack == []