class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        current_max = max(nums)
        for i in nums:
            current_sum = current_sum + i
            current_sum = max(0,current_sum)
            current_max = max(current_sum,current_max)
            
        if current_max > 0:
            return current_max
        else:
            return max(nums)
            
        
        
