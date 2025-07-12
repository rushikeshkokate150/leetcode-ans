class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        l, r = 0, 0
        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                l += 1  
            r += 1 
        return l  
