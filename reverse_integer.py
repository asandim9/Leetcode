class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x > (2**31)-1):
            return 0
        elif(x < pow(2,31)*(-1)):
            return 0 
        else:
            a = abs(x)
            temp = 0
            while(a>0):
                dig = a%10
                temp = temp*10 + dig
                a = a/10
            if(temp > (2**31)-1):
                return 0
            #elif()
            elif(x<0):
                return temp*(-1)
            else:
                return temp
            