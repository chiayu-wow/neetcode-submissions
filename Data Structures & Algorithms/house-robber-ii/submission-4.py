class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def count(num):
            if not num:
                return 0

            n = len(num)
            if n == 1:
                return num[0]
            if n < 3:
                return max(num[0], num[1])

            dp = [0] * (n)

            dp[0] = num[0]
            dp[1] = num[1]

            for i in range(2, n):
                for j in range(i-2, -1, -1):
                    dp[i] = max(dp[i], dp[j] + num[i]) 
            return max(dp)
        print(nums[1:], nums[:len(nums)-1])
        return max(count(nums[:len(nums)-1]), count(nums[1:]))