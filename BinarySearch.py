# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 07:20:36 2023

@author: mpspb
"""

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l 
        