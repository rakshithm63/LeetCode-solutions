class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        p1=0
        p2=0
        l=len(nums)
        p1=nums[0]*nums[1]
        p2=nums[l-1]*nums[l-2]
        return p2-p1