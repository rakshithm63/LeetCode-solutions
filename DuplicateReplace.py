# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:12:26 2023

@author: mpspb
"""

class Solution(object):
    def removeDuplicates(self, nums):
         # Initialize a pointer i at the beginning of the array
        i = 0

        # Iterate through the array starting from the second element (j = 1)
        for j in range(1, len(nums)):
            # If the current element is different from the previous element
            if nums[j] != nums[i]:
                # Increment i to move to the next unique element
                i += 1
                # Update the current position (i) with the unique element (nums[j])
                nums[i] = nums[j]

        # Return the length of the modified array (i + 1)
        return i + 1