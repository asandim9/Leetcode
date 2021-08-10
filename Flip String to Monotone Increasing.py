class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zeros = s.count("0")
        ones_to_zeros = 0
        res = zeros
        
        for i in s:
            zeros -= i == "0"
            ones_to_zeros += i == "1"
            res = min(res,zeros + ones_to_zeros)
            
        return res
