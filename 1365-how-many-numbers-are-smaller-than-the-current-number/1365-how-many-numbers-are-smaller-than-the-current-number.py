class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        mydict = dict()
        for k, v in enumerate(sorted(nums)):
            if v not in mydict:
                mydict[v] = k
        return [mydict[item] for item in nums]

        