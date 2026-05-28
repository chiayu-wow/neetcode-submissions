import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        query = [(queries[i], i) for i in range(len(queries))]
        query.sort(key = lambda x : x[0])
        n, m = len(queries), len(intervals)

        heap = []

        i = 0 #index for interval

        ans = [-1]*n

        for cur, idx in query:
            while i < m and intervals[i][0] <= cur:
                ## store (size, right)
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] +1, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < cur:
                heapq.heappop(heap)

            if heap:
                ans[idx] = heap[0][0]
        return ans
                
            


        

        
        