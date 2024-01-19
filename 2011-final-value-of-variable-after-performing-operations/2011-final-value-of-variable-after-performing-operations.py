class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for var in operations:
            if var == "X++" or var == "++X":
                x += 1
            else:
                x -= 1
        return x
        