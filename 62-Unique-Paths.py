'''
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range (m)] for _ in range (n)]
        dp[n-1] = [1 for _ in range (m)]
        for i in range (n):
            dp[i][m-1] = 1
        
        for i in range (n-2, -1, -1):
            for j in range (m-2, -1, -1):
                dp[i][j] = dp[i][j+1]+dp[i+1][j]
        return dp[0][0]