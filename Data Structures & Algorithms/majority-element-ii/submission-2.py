class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ## Majority Vote Algorithm
        n = len(nums)

        if n == 1 or n == 2:
            return nums
        
        ## maintain candidate
        c1, c2 = 0, 1
        count1, count2 = 0, 0

        for idx in range(n):
            cur = nums[idx]
            if cur == c1:
                count1 += 1
            elif cur == c2:
                count2 += 1
            elif count1 == 0:
                c1 = cur
                count1 += 1
            elif count2 == 0:
                c2 = cur
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        ## check
        count1, count2 = 0, 0

        for i in range(n):
            if nums[i] == c1:
                count1 += 1
            if nums[i] == c2:
                count2 += 1
        ans = []

        if count1 > n/3:
            ans.append(c1)
        if count2 > n/3:
            ans.append(c2)

        return ans
        