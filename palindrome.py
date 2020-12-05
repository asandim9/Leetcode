class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        reverse = 0
        if (x < 0):
            return False
        
        else:
            
            while(x>0):
                dig = x%10
                reverse = reverse*10 + dig
                x = x/10
                
            if(temp == reverse):
                return True
            else:
                return False