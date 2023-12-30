# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 09:08:44 2023

@author: mpspb
"""

class Solution(object):
    def singleNumber(self, nums):
        num = 0;
        for i in nums:
            num ^= i;
        return num;