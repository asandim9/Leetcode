class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = len(nums)
        result = []
        res = []
        
        #Iterate through nums
        for i in range(0,a):
            for j in range(i+1,a):
                if nums[j] == (target - nums[i]):
                    result.append(i)
                    result.append(j)
        
        [res.append(x) for x in result if x not in res]       #To aavoid repetitions 
        
            
            
                    
                    
        return res