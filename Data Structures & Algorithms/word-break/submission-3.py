class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dic = set(wordDict)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i, 0 , -1):
                if s[j-1:i] in dic and dp[j-1]:
                    dp[i] = True
                    break
        return dp[-1]

        