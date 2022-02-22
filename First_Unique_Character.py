class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = ""
        res = -1
        for i in s:
            a = s.count(i)
            if a == 1:
                temp = i
                res = s.index(temp)
                break
            else:
                res = -1
                
        return res
                
                
        
        
