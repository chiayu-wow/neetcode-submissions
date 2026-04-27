class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        result = [False] * n
        result[0] = True
        for i in range(n-1): 
            if not result[i]:
                continue
                
            cur = i+1    
            while cur < n and cur - i <= nums[i]:
                result[cur] = True
                cur += 1

        return result[-1]

        