class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        「先看是不是舊人」（維護現有勢力，避免同一個數字分身佔據多個位置）

        「再看有無空缺」（有人倒下了，新勢力才能插旗填補空位）

        「最後看是不是破壞者」（既不是舊人也沒空缺，那就是進來引發三方混戰、同歸於盡的第三勢力）
        """
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
        