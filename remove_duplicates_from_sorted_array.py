class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        j = 0
        for i in range(a):
            if (nums[i] != nums[j]):
                j = j+1
                nums[j] = nums[i]
                
        return j+1
            