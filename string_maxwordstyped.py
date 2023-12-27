# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:30:04 2023

@author: mpspb
"""

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        
        broke=set(brokenLetters)
        return sum(not set(w) & broke for w in text.split())