class Solution:
    def firstUniqChar(self, s: str) -> int:
        unq = {}
        for char in s:
            unq[char] = unq.get(char, 0) + 1

        for i, char in enumerate(s):
            if unq[char] == 1:
                return i

        return -1