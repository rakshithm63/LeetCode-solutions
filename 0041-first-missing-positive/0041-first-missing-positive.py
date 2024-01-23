class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums1=set(nums)
        for num in range(1,2**31):
            if num not in nums1:
                return num
        