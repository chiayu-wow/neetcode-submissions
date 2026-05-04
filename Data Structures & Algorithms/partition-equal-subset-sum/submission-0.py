class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        print(sum(nums))
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2

        dp = [False] * (target+1)
        dp[0] = True

        n = len(nums)

        for i in range(n):
            cur = nums[i]
            for j in range(target, -1, -1):
                if dp[j] and j + cur <= target:
                    dp[j+cur] = True
        print(dp)
        return dp[-1]

            
        