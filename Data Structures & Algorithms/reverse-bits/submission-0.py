class Solution:
    def reverseBits(self, n: int) -> int:
        
        tmp = bin(n)[2:].zfill(32)
        print(tmp)
        tmp = tmp[::-1]
        print(tmp)
        return int(tmp,2)
        
        