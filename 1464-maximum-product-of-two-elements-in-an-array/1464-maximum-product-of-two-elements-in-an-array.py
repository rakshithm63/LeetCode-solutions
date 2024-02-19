class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=len(nums)
        p1=0
        nums.sort()
        p1=(nums[l-1]-1)*(nums[l-2]-1)
        return p1
        