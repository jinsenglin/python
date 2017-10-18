import copy

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort()
        s.sort()
        
        maximum = 0
        for size_wanted in g:
            while len(s) > 0:
                size = s[0]
                del(s[0])
                
                if size >= size_wanted:
                    maximum += 1
                    break
        
        return maximum
