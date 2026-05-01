class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)
        cur = newInterval
        ans = []
        for i in range(n):
            start, end = intervals[i]

            if not cur:
                ans.append(intervals[i])
                continue
                
            if cur[1] < start:
                ans.append(cur)
                cur = None
                ans.append(intervals[i])
                continue    
            if cur[0] > end:
                ans.append(intervals[i])
                continue
            
            ## encounter overlapping
            if cur:
                cur = (min(start, cur[0]), max(end, cur[1]))

        if cur:
            ans.append(cur)
        return ans