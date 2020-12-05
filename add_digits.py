class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num
        temp = 0
        temp1 = 0
        temp2 = 0
        while(x>0):
            dig = x%10
            temp = temp + dig
            x = x/10
            
        
        if(temp>=10):
            dig1 = temp%10
            temp1 = temp1 + dig1
            temp = temp/10
            temp1 = temp1 + temp
            temp = temp1
        if(temp1 >= 10):
            dig2 = temp1%10
            temp2 = temp2 + dig2
            temp1 = temp1/10
            temp2 = temp2 + temp1
            temp = temp2
        
        return temp       
        