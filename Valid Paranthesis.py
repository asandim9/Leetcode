class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        else:
            res = []
            for i in s:
                if res == []:
                    res.append(i)
                    
                else:
                    if i == ')':
                        if res[-1] == '(':
                            res.pop()
                        else: return False
                            
                    elif i == ']':
                        if res[-1] == '[':
                            res.pop()
                        else: return False
                            
                    elif i == '}':
                        if res[-1] == '{':
                            res.pop()
                        else: return False
                    else:
                        res.append(i)
                            
            if res == []:
                return True
            else:
                return False

            
