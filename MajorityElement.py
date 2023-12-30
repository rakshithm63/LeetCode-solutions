# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 09:18:08 2023

@author: mpspb
"""

class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]