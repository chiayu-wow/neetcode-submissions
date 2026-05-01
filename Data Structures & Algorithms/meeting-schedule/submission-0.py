"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        n = len(intervals)
        st = []

        for i in range(n):
            cur = intervals[i]

            if not st:
                st.append(cur)
                continue

            if st[-1].start >= cur.end or st[-1].end <= cur.start:
                st.append(cur)
            else:
                return False

        return True
