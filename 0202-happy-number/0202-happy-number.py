class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(len(str(n)) > 1):
            y = 0
            for i in str(n):
                y += int(i) ** 2
            n = y

        if n == 1 or n == 7:
            return True
        else:
            return False   