class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        largestsstring = 0
        maxfreq = 0
        l = 0
        b = {}
 
        for r in range(len(s)):
            if s[r] not in b:
                b[s[r]] = 1
            else:
                b[s[r]]+=1

            maxfreq= max(b.values())
            
            while ((r-l)+1) - maxfreq > k:
                b[s[l]] -=1
                maxfreq= max(b.values())
                l+=1
            largestsstring= max(largestsstring,(r-l)+1)
        return largestsstring