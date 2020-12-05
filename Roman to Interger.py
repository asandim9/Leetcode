class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        a = len(s)
        integer = 0
        for i in range(a):
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                integer += roman[s[i]] - 2 * roman[s[i - 1]]
                
            else:
                integer += roman[s[i]]
                
        return integer
        