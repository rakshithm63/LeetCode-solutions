# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:35:22 2023

@author: mpspb
"""

class Solution(object):
    def strStr(self, haystack, needle):
      
        for i in range(len(haystack) - len(needle) + 1): 
            if haystack[i : i+len(needle)] == needle:
                return i
        
        return -1