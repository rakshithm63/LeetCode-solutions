# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 09:32:31 2023

@author: mpspb
"""

class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)