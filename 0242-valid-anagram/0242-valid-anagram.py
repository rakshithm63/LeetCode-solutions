class Solution(object):
    def isAnagram(self, s, t):
        flag=True
        if len(set(s))!=len(set(t)):
            return False
        else:
            for char in set(s):
                if s.count(char)!=t.count(char):
                    flag = False
                
        return flag
        
        