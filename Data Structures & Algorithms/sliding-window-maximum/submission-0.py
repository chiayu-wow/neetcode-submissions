import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        qu = []
        ans = []

        for right in range(n):

            heapq.heappush(qu, (-nums[right], right))

            if right >= k - 1 :
                while qu[0][1] < right - k + 1:
                    heapq.heappop(qu)
                ans.append(-qu[0][0])
        return ans
        
        