class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            minv = i
            for j in range(i,len(nums)):
                if nums[minv] > nums[j]:
                    minv = j
            nums[i], nums[minv] = nums[minv],nums[i]