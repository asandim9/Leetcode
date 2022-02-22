class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        pro = 1
        for i in reversed(columnTitle):
            res += ((ord(i) - ord('A')) + 1) * pro
            pro *=26
            
        return res
            
        
