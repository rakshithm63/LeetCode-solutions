class Solution(object):
    def numIdenticalPairs(self, nums):
        n=len(nums)
        count=0
        for i in range(0,n-1):
            for j in range(i,n):
                if(nums[i]==nums[j] and i<j):
                    count+=1;
        return count

        