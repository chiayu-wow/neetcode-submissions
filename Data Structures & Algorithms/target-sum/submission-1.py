class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = len(nums)
        self.ans = 0
        def helper(idx, remain):
            if idx == m:
                if remain == 0:
                    self.ans += 1
                return

            helper(idx+1, remain + nums[idx])
            helper(idx+1, remain - nums[idx])
        
        helper(1, target - nums[0])
        helper(1, target + nums[0])

        return self.ans