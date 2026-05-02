class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(n+1):
            tmp = bin(i)[2:]
            ans[i] = tmp.count("1")
        return ans