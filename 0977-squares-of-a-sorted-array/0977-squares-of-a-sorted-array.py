class Solution(object):
    def sortedSquares(self, nums):
        nums.sort()
        res=[]
        for i in nums:
            i=i*i
            res.append(i)
        res.sort()
        return(res)    
            
        
        
        