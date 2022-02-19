# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        start = 0
        end = n
        mid = n//2
        
        while start <= end:
            print(mid)
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            
            elif isBadVersion(mid) and isBadVersion(mid-1):
                end = mid-2
                
            elif not isBadVersion(mid):
                start = mid+1
            mid = int((end+start)/2)
            
        if start - end==1:
            return start
                
            
            
        
