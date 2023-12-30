# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 07:09:52 2023

@author: mpspb
"""

class Solution:
    def makeEqual(self, words):
        counts = {}
        
        for word in words:
            for c in word:
                counts[c] = counts.get(c, 0) + 1
        
        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        
        return True