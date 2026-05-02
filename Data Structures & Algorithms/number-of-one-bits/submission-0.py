class Solution:
    def hammingWeight(self, n: int) -> int:
        tmp = bin(n)[2:]
        return tmp.count("1")

        