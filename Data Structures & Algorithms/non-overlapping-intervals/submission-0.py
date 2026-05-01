class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : x[0])
        n = len(intervals)
        st = []
        ans = 0

        for i in range(n):
            cur = intervals[i]

            if not st:
                st.append(cur)
                continue

            if st[-1][0] >= cur[1] or st[-1][1] <= cur[0]:
                st.append(cur)
                continue
            
            ans += 1

            if st[-1][1] > cur[1]:
                st.pop()
                st.append(cur)
        return ans