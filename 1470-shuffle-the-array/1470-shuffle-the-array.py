class Solution(object):
    def shuffle(self, nums, n):
        array1 = nums[:n]
        array2 = nums[n:]
        result = []
        for i in range(len(array1)):
            result.append(array1[i])
            result.append(array2[i])

        return result
        