class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a = len(nums)
        count = 0
        for i in range(0,a):
            if(nums[i] != val):
                nums[count] = nums[i]
                count +=1
                
        return count