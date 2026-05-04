class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(num):
            result = 0
            cur = num
            while cur > 0:
                tmp = cur % 10
                result += tmp ** 2
                cur = cur // 10
            return result

        seen = set()

        cur = n 
        seen.add(cur)

        while cur != 1:
            cur = cal(cur)

            if cur in seen:
                return False
            seen.add(cur)

        return True
        