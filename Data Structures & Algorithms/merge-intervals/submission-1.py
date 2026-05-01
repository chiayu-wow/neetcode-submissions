class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        n = len(intervals)
        st = []

        for i in range(n):
            cur = intervals[i]

            if not st:
                st.append(cur)
           
            while st:
                ## not overlap
                if st[-1][0] > cur[1] or st[-1][1] < cur[0]:
                    break
                
                peak = st.pop()
                cur[0] = min(peak[0], cur[0])
                cur[1] = max(peak[1], cur[1])           
            
            st.append(cur)
        return st