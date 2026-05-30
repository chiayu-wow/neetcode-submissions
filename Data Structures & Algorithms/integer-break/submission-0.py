class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-math.inf] * (n+1)

        dp[2] = 1

        for i in range(3, n+1):
            for j in range(2, i+1):
                dp[i] = max(dp[i], (i-j) * dp[j], (i-j) * j)
        
        return dp[-1]
        