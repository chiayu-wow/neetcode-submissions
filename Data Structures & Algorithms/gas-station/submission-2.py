class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        for start in range(n):
            remain = 0
            isValid = True
            for k in range(n):
                remain += gas[(start + k)%n]
                remain -= cost[(start + k)%n]
                if remain < 0:
                    isValid = False
                    break
            if isValid:
                return start        
        return -1

