class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [math.inf] * n
        dp[0] = 0

        for i in range(n):
            for k in range(1, nums[i]+1):
                if i + k >= n:
                    break 
                dp[i+k] = min(dp[i+k], dp[i] + 1)
        return dp[-1]