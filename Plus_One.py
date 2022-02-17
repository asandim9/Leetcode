class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_ints = [str(i)for i in digits]
        
        str1 = "".join(string_ints)
        num = int(str1)
        res = num + 1
        res_final = [int(x) for x in str(res)]
        
        return res_final
        
        
        
                  
        
        
