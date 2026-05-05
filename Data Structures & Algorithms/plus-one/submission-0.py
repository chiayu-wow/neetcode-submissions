class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = deque(digits)
        for i in range(len(digits)-1, -1, -1):
            ans[i] += carry
            if ans[i] > 9:
                ans[i] = ans[i] % 10
                carry = 1
            else:
                carry = 0
        
        if carry != 0:
            ans.appendleft(carry)
        return list(ans)
            
        