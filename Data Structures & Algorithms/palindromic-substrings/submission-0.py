class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        n = len(s)
        for i in range(n-1):
            left, right = i-1, i+1
            while 0 <= left and right < n and s[left] == s[right]:
                ans += 1
                right += 1
                left -= 1

            ## if s[i] == s[i+1]
            if s[i] != s[i+1]:
                continue
            ans += 1
            left, right = i-1, i+2
            while 0 <= left and right < n and s[left] == s[right]:
                ans += 1
                right += 1
                left -= 1

        return ans


        