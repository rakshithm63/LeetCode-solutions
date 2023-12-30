# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 07:15:30 2023

@author: mpspb
"""

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
        
        