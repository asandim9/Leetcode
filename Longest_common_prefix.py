class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return " "
        else:
            current = strs[0]
            for i in range(0,len(strs)):
                temp = ""
                for j in range(0,len(strs[i])):
                    if j < len(current) and current[j] == strs[i][j]:
                        temp += current[j]
                        
                    else:
                        break
                current = temp
                
            return current
                        
            
                
        
