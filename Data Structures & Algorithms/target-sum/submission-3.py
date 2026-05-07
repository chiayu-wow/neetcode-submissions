class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        if target > total:
            return 0
        if (total + target) % 2 != 0:
            return 0
        
        p = (total + target) // 2

        n = len(nums)
        dp = [0] * (p+1)
        dp[0] = 1

        for n in nums:
            for k in range(p, n - 1, -1):
                dp[k] += dp[k - n]
        return dp[-1]