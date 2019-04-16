'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.rob_row(nums[1:]), self.rob_row(nums[:-1]))

    def rob_row(self, nums):
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])
        return res[-1]