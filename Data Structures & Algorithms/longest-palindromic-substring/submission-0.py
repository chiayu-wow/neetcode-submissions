class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        n = len(s)
        for i in range(n-1):
            tmp = deque([s[i]])
            left, right = i-1, i+1
            while 0 <= left and right < n and s[left] == s[right]:
                tmp.append(s[right])
                tmp.appendleft(s[left])
                right += 1
                left -= 1
            
            if len(tmp) > len(ans):
                ans = "".join(tmp)

            ## if s[i] == s[i+1]
            if s[i] != s[i+1]:
                continue
                
            tmp = deque([s[i], s[i+1]])
            left, right = i-1, i+2
            while 0 <= left and right < n and s[left] == s[right]:
                tmp.append(s[right])
                tmp.appendleft(s[left])
                right += 1
                left -= 1
            
            if len(tmp) > len(ans):
                ans = "".join(tmp)
        return ans


        