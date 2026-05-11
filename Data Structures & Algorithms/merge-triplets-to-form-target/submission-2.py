class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        cur = [0,0,0]
        for i in range(n):
            if cur == target:
                return True

            if max(cur[0], triplets[i][0]) > target[0]:
                continue

            if max(cur[1], triplets[i][1]) > target[1]:
                continue

            if max(cur[2], triplets[i][2]) > target[2]:
                continue
            
            cur[0] = max(cur[0], triplets[i][0])
            cur[1] = max(cur[1], triplets[i][1])
            cur[2] = max(cur[2], triplets[i][2])
            
        return False if cur != target else True