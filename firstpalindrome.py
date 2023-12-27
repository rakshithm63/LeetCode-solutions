# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:37:26 2023

@author: mpspb
"""

class Solution(object):
    def firstPalindrome(self, words):
     
        for word in words:
            if word==word[::-1]:
                return word
        return ""        
        