# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:32:02 2023

@author: mpspb
"""

class Solution(object):
    def mostWordsFound(self, sentences):
    
        answer=0
        for sentence in sentences:
            answer = max(answer, len(sentence.split()))

        return answer