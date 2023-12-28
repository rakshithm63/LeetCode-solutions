# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:01:56 2023

@author: mpspb
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return[]