"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range (0, len(nums))]
        dp[0] = nums[0]
        for i in range (1, len(dp)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        
        return max(dp)